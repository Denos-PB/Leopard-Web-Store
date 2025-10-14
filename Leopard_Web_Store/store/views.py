from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, AddToCartSerializer
from .decorators import admin_required, role_required

User = get_user_model()


"""Список товарів"""
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gender', 'size', 'price']

"""Додавання у кошик"""
class AddToCartView(APIView):
    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            # Тимчасово беремо першого користувача (до додавання логіну)
            user = User.objects.first()

            # Знайти або створити кошик користувача
            cart, _ = Cart.objects.get_or_create(user=user)

            # Знайти товар
            product = Product.objects.get(id=product_id)

            # Знайти або створити CartItem
            item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                item.quantity += quantity
            else:
                item.quantity = quantity
            item.save()

            return Response(
                {
                    "message": f"Товар '{product.name}' додано в кошик.",
                    "quantity": item.quantity
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","password")
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        refresh['user_id'] = user.id
        refresh['roles'] = [user.role]
        access_token_obj = refresh.access_token
        access_token_obj['user_id'] = user.id
        access_token_obj['roles'] = [user.role]

        return Response({
            'refresh': str(refresh),
            'access': str(access_token_obj),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        }, status=status.HTTP_200_OK)

class AdminOnlyView(APIView):
    @admin_required
    def get(self, request):
        return Response({'message': 'This is an admin-only endpoint', 'user_id': request.user_id}, status=status.HTTP_200_OK)

class ModeratorView(APIView):
    @role_required(['admin', 'moderator'])
    def get(self, request):
        return Response({'message': 'This endpoint requires admin or moderator role', 'user_id': request.user_id}, status=status.HTTP_200_OK)
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, AddToCartSerializer


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

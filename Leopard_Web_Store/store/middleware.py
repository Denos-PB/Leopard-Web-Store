from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.http import JsonResponse
from django.conf import settings

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        exempt_paths = ['/api/auth/login/', '/api/auth/register/', '/api/auth/refresh/', '/api/products/', '/admin/']
        if any(request.path.startswith(path) for path in exempt_paths):
            return self.get_response(request)

        # Only apply JWT auth to API endpoints, not static files or root path
        if not request.path.startswith('/api/'):
            return self.get_response(request)

        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)

        token = auth_header.split(' ')[1]

        try:
            # Validate token
            access_token = AccessToken(token)
            request.user_id = access_token['user_id']
            request.user_roles = access_token.get('roles', [])
        except (InvalidToken, TokenError) as e:
            return JsonResponse({'error': 'Invalid or expired token'}, status=401)

        response = self.get_response(request)
        return response
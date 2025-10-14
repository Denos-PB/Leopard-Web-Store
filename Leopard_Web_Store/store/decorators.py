from functools import wraps
from django.http import JsonResponse
from rest_framework import status

def role_required(required_roles):
    """
    Decorator to check if user has required roles.
    required_roles can be a string or list of strings.
    """
    if isinstance(required_roles, str):
        required_roles = [required_roles]

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_roles = getattr(request, 'user_roles', [])
            if not any(role in user_roles for role in required_roles):
                return JsonResponse(
                    {'error': f'Access denied. Required roles: {required_roles}'},
                    status=status.HTTP_403_FORBIDDEN
                )
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def admin_required(view_func):
    """Shortcut decorator for admin-only access"""
    return role_required('admin')(view_func)

def moderator_required(view_func):
    """Shortcut decorator for moderator access"""
    return role_required(['admin', 'moderator'])(view_func)
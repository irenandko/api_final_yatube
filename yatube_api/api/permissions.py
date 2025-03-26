from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверка доступа: является ли инициатором запроса автор,
    в противном случае разрешено только"""

    def has_object_permission(self, request, view, obj):
        return (request.method
                in permissions.SAFE_METHODS
                or obj.author == request.user)

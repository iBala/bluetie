import logging

from rest_framework.permissions import IsAuthenticated


LOGGER = logging.getLogger(__name__)


class IsLoggedInUser(IsAuthenticated):
    """
    Allows access only to authenticated user.
    """

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        try:
            return is_authenticated and (request.user is not None)
        except ("Can't find user", AttributeError):
            return False


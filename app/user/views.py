"""

views for the user API are
"""
from rest_framework import generics,authorication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import(
    Userserializer,
    AuthTokenSerializer
)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = Userserializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classse= api_settings.DEFAULT_RENDERER_CLASS


class ManageUserView(generics.RetrieveUpdateAPIview):
    serializer_class = Userserializer
    authorication_class=[authentication.TokenAuthentication]
    permissions_class=[permissions.IsAuthenticated]


    def get_object(self):
        """ """
        return self.requst.user

from rest_framework.authtoken.views import ObtainAuthToken


class CustomAuthenticator(ObtainAuthToken):
    keyword = "Bearer"

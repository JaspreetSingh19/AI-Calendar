from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from authentication.serializers import LoginSerializer
from common.messages import SUCCESS_MESSAGES


class LoginViewSet(viewsets.ModelViewSet):
    """
    Allow only authenticated user to login.
    If the user is valid provide him the access and refresh token
    and save it to the database.
    """
    http_method_names = ['post']
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response('Successful login', LoginSerializer),
            401: openapi.Response('Unauthorized', LoginSerializer),
        },
        operation_summary="Authenticate and provide tokens",
        operation_description="This endpoint allows an authenticated user to login and provides access and refresh "
                              "tokens.",
    )
    def create(self, request, *args, **kwargs):
        """
        Create method to provide access token and refresh
        token to the authenticated user by checking their
        credentials.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(serializer.validated_data)
            return Response(
                {'data': user, 'success': SUCCESS_MESSAGES['login']['success']}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

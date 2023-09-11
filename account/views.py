from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serializers import RegistrationSerializer
from common.messages import SUCCESS_MESSAGES


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    RegistrationViewSet class to register a new user
    """
    http_method_names = ['post']
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        """
        creates a new requested user and call the
        serializer class
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['registration']['successfully'], 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

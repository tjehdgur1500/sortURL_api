from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from sorten.paginations import IdPagination
from .serializer import UserSerializer
from .permissions import IsOwner
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]
    pagination_class = IdPagination

    @action(methods=['DELETE'], detail=False)
    def logout(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
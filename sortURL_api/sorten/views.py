from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Sorten
from .paginations import IdPagination
from .serializer import SortenSerializer
from .permissions import IsOwner


class SortenViewSet(ModelViewSet):
    queryset = Sorten.objects.all()
    serializer_class = SortenSerializer
    permission_classes = [IsOwner]
    pagination_class = IdPagination

    def get_queryset(self):
        if not self.request.user.id == None:
            user = self.request.user
            queryset = Sorten.objects.filter(owner=user)
            return queryset
        else:
            return super().get_queryset()

    def perform_create(self, serializer):

        serializer.save(
            owner=self.request.user
        )

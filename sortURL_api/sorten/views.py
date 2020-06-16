from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from random import randint
from .models import Sorten
from .paginations import IdPagination
from .serializer import SortenSerializer
from .permissions import IsOwner
import base62

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

        a = Sorten.objects.last()
        marge = a.id+1
        marge = base62.encode(marge)
        serializer.save(
            owner=self.request.user,
            shorturl=marge,
        )
    # url shorten
    # def create_short_url(self):
    #
    #     random_int = self.random_num_create()
    #
    #     Sorten.objects.get(random_int=random_int)
    #
    #     url_obj = Sorten(random_int=random_int)
    #     url_obj.save()
    #     return url_obj
    #
    # def random_num_create(self):
    #     num = self.randint(1, 218340105584895)
    #     return num


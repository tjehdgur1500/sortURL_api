import base62
from collections import Counter
from django.http import HttpResponseRedirect
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Sorten
from .paginations import IdPagination
from .permissions import IsOwner
from .serializer import SortenSerializer


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
        if a is None:
            merge = 1
        else:
            merge = a.id + 1
        merge = base62.encode(merge)

        if self.request.user.is_anonymous:
            c = None
        else:
            c = self.request.user

        serializer.save(
            owner=c,
            shorturl=merge,

        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        short_url = f"{request.scheme}://{request.get_host()}/sorts/cuturl/{response.data['shorturl']}"
        response.data['shorturl'] = short_url
        return response


class RetriveViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Sorten.objects.all()
    serializer_class = SortenSerializer
    lookup_field = 'shorturl'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.count += 1
        instance.save()
        return HttpResponseRedirect(serializer.data['selfurl'])
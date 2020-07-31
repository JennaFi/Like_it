from rest_framework.decorators import action
from rest_framework.response import Response

from .. import services
from .serializers import FavSerializer


class LikedMixin:

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):

        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        if request.method == 'POST':
            obj = self.get_object()
            services.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['get'])
    def favs(self, request, pk=None):
        if request.method == 'GET':

            obj = self.get_object()
            favs = services.get_favs(obj)
            serializer = FavSerializer(favs, many=True)
        return Response(serializer.data)

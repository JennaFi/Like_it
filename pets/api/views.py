from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from pet_likes.api.mixins import LikedMixin
from ..models import Pet
from .serializers import PetSerializer


class PetViewSet(LikedMixin,
                   viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

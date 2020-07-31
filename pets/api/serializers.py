from rest_framework import serializers
from ..models import Pet
from pet_likes import services as likes_services


class PetSerializer(serializers.ModelSerializer):
    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = (
            'id',
            'body',
            'total_likes',
            'is_fav'

        )

    def get_is_fav(self, obj) -> bool:

        user = self.context.get('request').user
        return likes_services.is_fav(obj, user)


from rest_framework import serializers

from pets.models import UserPets


class UserPetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPets
        fields = '__all__'

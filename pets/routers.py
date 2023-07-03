from rest_framework import routers

from pets.views import UserPetsViewSet

user_pets_router = routers.SimpleRouter()
user_pets_router.register(r'', UserPetsViewSet)

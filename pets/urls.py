from django.urls import path, include

from pets.routers import user_pets_router


urlpatterns = [
    path('', include(user_pets_router.urls)),
]




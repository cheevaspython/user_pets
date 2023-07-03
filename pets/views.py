from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pets.models import UserPets
from pets.serializers import UserPetsSerializer
from users.models import CustomUser
from users.serializers import CustomUserPetsSerializer
from pets.services import UserPetsTypeFilter


class UserPetsViewSet(viewsets.ModelViewSet):
    queryset = UserPets.objects.all()
    serializer_class = UserPetsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserPetsTypeFilter
    http_method_names = ['get', 'post', 'delete', 'patch', 'head']
    
    @action(detail=True, methods=['get'])
    def list_users_and_pets(self, request, pk=None) -> Response:  
        """
        Show CustomUser's and Pets. 
        If pk -> all -> show all CustomUser's.
        """
        if pk == 'all':
            users = CustomUserPetsSerializer(CustomUser.objects.all(), many=True)
        else:
            users = CustomUserPetsSerializer(CustomUser.objects.get(pk=pk))
        return Response({'users_and_pets': users.data}, status=status.HTTP_200_OK)    






from django_filters import rest_framework as filters

from pets.models import UserPets


class UserPetsTypeFilter(filters.FilterSet):
    """Фильтр по типу."""
    
    weight = filters.NumericRangeFilter()

    class Meta:
        model = UserPets
        fields = ['pet_type']
    



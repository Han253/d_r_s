import django_filters
from .models import Mascota

class MascotaFilter(django_filters.FilterSet):
    # Rangos numéricos
    min_edad = django_filters.NumberFilter(field_name='edad', lookup_expr='gte')
    max_edad = django_filters.NumberFilter(field_name='edad', lookup_expr='lte')

    # Búsqueda parcial en texto
    brand = django_filters.CharFilter(field_name='sexo', lookup_expr='icontains')
    model = django_filters.CharFilter(field_name='raza', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='especie', lookup_expr='icontains')

    class Meta:
        model = Mascota
        fields = []  # se definen explícitamente arriba
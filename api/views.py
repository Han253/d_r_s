from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MascotaSerializer

from .models import Mascota 
from .filters import MascotaFilter



# Create your views here.

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MascotaFilter  # Usar el filtro definido en filters.py
    
    ordering_fields = ['edad', 'fecha_registro']  # Habilitar ordenamiento
    ordering = ['fecha_registro']  # Orden por defecto
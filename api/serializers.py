from rest_framework import serializers
from .models import Mascota

# Serializador
class MascotaSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Mascota
        fields = '__all__'
        read_only_fields = ['fecha_registro']
from rest_framework import serializers

from .models import Equipo


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = [
            "id",
            "codigo_inventario",
            "nombre",
            "categoria",
            "estado",
            "ubicacion",
            "cantidad",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = ["id", "creado_en", "actualizado_en"]

from django.db import models


class Equipo(models.Model):
    class Estado(models.TextChoices):
        DISPONIBLE = "disponible", "Disponible"
        PRESTADO = "prestado", "Prestado"
        MANTENCION = "mantencion", "En mantención"
        BAJA = "baja", "Dado de baja"

    codigo_inventario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=120)
    categoria = models.CharField(max_length=80)
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.DISPONIBLE
    )
    ubicacion = models.CharField(max_length=120)
    cantidad = models.PositiveIntegerField(default=1)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["codigo_inventario"]

    def __str__(self):
        return f"{self.codigo_inventario} - {self.nombre}"

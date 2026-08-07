from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Equipo


class EquipoApiTests(APITestCase):
    def setUp(self):
        self.equipo = Equipo.objects.create(
            codigo_inventario="INF-001",
            nombre="Notebook de laboratorio",
            categoria="Computador portátil",
            estado=Equipo.Estado.DISPONIBLE,
            ubicacion="Laboratorio 204",
            cantidad=1,
        )
        self.payload = {
            "codigo_inventario": "INF-002",
            "nombre": "Proyector Epson",
            "categoria": "Proyector",
            "estado": "disponible",
            "ubicacion": "Bodega TI",
            "cantidad": 2,
        }

    def test_01_lista_equipos(self):
        response = self.client.get(reverse("equipo-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_02_crea_equipo(self):
        response = self.client.post(reverse("equipo-list"), self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Equipo.objects.filter(codigo_inventario="INF-002").exists())

    def test_03_obtiene_equipo_por_id(self):
        response = self.client.get(reverse("equipo-detail", args=[self.equipo.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["codigo_inventario"], "INF-001")

    def test_04_actualiza_equipo_parcialmente(self):
        response = self.client.patch(
            reverse("equipo-detail", args=[self.equipo.id]),
            {"estado": "prestado"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.equipo.refresh_from_db()
        self.assertEqual(self.equipo.estado, Equipo.Estado.PRESTADO)

    def test_05_elimina_equipo(self):
        response = self.client.delete(reverse("equipo-detail", args=[self.equipo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Equipo.objects.filter(id=self.equipo.id).exists())

    def test_06_rechaza_codigo_inventario_duplicado(self):
        self.payload["codigo_inventario"] = "INF-001"
        response = self.client.post(reverse("equipo-list"), self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("codigo_inventario", response.data)

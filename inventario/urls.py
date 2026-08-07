from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EquipoViewSet, health_check, version

router = DefaultRouter()
router.register("equipos", EquipoViewSet, basename="equipo")

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("version/", version, name="version"),
    path("", include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TechnologyViewSet, ProjectViewSet

app_name = "projects"

router = DefaultRouter()
router.register(r"technologies", TechnologyViewSet)
router.register(r"", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
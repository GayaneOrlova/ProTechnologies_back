from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from projects.models import Technology, Project
from .permissions import IsAuthorOrReadOnly
from projects.serializers import (
    TechnologyReadSerializer,
    ProjectReadSerializer,
    ProjectWriteSerializer,
)

class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve post technologies
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologyReadSerializer
    permission_classes = (permissions.AllowAny,)
    

class ProjectViewSet(viewsets.ModelViewSet ):
    """
    CRUD posts
    """
    queryset = Project.objects.all()
    pagination_class = PageNumberPagination
    
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ProjectWriteSerializer
        return ProjectReadSerializer

    # get_permissions(self) method helps you separate 
    # permissions for different actions inside the same view.
    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.IsAuthenticated,)
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (IsAuthorOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()


        
    




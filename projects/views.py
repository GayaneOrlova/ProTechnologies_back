from rest_framework import permissions, viewsets
from projects.models import Technology, Project
from .permissions import IsAuthorOrReadOnly
# from services import MyPagination
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from projects.serializers import (
    TechnologyReadSerializer,
    ProjectReadSerializer,
    ProjectWriteSerializer,
)

# class MyPagination(LimitOffsetPagination, PageNumberPagination):
#     page_size = 2
#     max_page_size = 20
#     def get_pagination(self, data):
#         # response = super().get_pagination(data)
#         # response.data['offset'] = self.get_offset(self.request)
#         return Response({
#             'links': {
#               'next': self.get_next_link(),
#               'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'results': data,
#             'offset': self.get_offset()
#         })

class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve post technologies
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologyReadSerializer
    permission_classes = (permissions.AllowAny,)
    

class ProjectViewSet(viewsets.ModelViewSet,LimitOffsetPagination ):
    """
    CRUD posts
    """
    queryset = Project.objects.all()
    # pagination_class = MyPagination
    # pagination_class = LimitOffsetPagination
    
    # In order to use different serializers for different 
    # actions, you can override the 
    # get_serializer_class(self) method
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
        
    




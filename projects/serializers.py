
from rest_framework import serializers
from .models import Technology, Project

class TechnologyReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"
class ProjectReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    technologies = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Project
        fields = "__all__"

    def get_technologies(self, obj):
        technologies = list(
            tech.name for tech in obj.technologies.get_queryset().only("name")
        )
        return technologies

class ProjectWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = "__all__"

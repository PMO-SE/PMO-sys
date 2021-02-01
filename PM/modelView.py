from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Project

#定义序列化器
class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('id', 'Region', 'Project_name', 'Project_leader', 'Project_type', 'Plant', 'BU')

#视图集(增删改查流程封装的)
class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
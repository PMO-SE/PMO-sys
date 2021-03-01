from rest_framework import serializers
from PM.models import Project


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ('Project_name','Project_type','add_time') # 返回给前端的json中包含的字段
        fields = "__all__" # 包含所有字段
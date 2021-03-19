from rest_framework import serializers
from PM.models import Project, Workload, CardInfo


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ('Project_name','Project_type')
        fields = "__all__"


class WorkloadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workload
        fields = "__all__"


class CardInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        fields = "__all__"

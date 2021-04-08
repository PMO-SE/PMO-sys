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
    Project_name = serializers.CharField(source='Project_ID.Project_name')
    Region = serializers.CharField(source='Project_ID.Region')
    Project_leader = serializers.CharField(source='Project_ID.Project_leader')
    Current_status = serializers.CharField(source='Project_ID.Current_status')
    Cluster = serializers.CharField(source='Project_ID.Cluster')
    BU = serializers.CharField(source='Project_ID.BU')
    Lob = serializers.CharField(source='Project_ID.Lob')
    Plant = serializers.CharField(source='Project_ID.Plant')
    target_COGS = serializers.FloatField(source='Project_ID.Additional_COGS')
    target_Prod = serializers.FloatField(source='Project_ID.Productivity')
    target_Capex = serializers.FloatField(source='Project_ID.CAPEX')
    target_Space = serializers.FloatField(source='Project_ID.Space_needed')
    target_Y_3_QTY = serializers.FloatField(source='Project_ID.Y_3_QTY')
    target_Expense = serializers.FloatField(source='Project_ID.Expense')
    target_Payback = serializers.FloatField(source='Project_ID.Payback')

    class Meta:
        model = CardInfo
        fields = "__all__"

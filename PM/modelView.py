from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Project
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect

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

class ProjectDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'project_card.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(project)
        return Response(serializer.data)

    def post(self, request, pk):

        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(project, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'project': project})
        serializer.save()
        return redirect('/ProMGT')
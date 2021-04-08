from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny
from PM import models
from django.db.models import Sum, Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from PM_admin.serializers import ProjectModelSerializer, CardInfoModelSerializer
from .models import Project, Workload, CardInfo


# 主页入口
def homepage(request):
    return render(request, 'Homepage.html')


# Project Dashboard入口
def project_dashboard(request):
    projects = models.Project.objects.all()
    project_num = projects.count()
    ongoing_num = project_num - projects.filter(Current_status='Close').count() - projects.filter(
        Current_status='Kickoff').count()
    COGS = round(models.Project.objects.aggregate(Sum('Additional_COGS')).get('Additional_COGS__sum'))
    productivity = round(models.Project.objects.aggregate(Sum('Productivity')).get('Productivity__sum') / 1000)
    CAPEX = round(models.Project.objects.aggregate(Sum('CAPEX')).get('CAPEX__sum') / 1000)
    proNum_BUs = models.Project.objects.annotate(count=Count('BU'))
    BUs = [];
    proNUM = []
    for proNum_BU in proNum_BUs:
        if proNum_BU.BU not in BUs:
            BUs.append(proNum_BU.BU)
            proNUM.append(projects.filter(BU=proNum_BU.BU).count())

    proNum_types = models.Project.objects.annotate(count=Count('Project_type'))
    types = [];
    proNUMtype = []
    for proNum_type in proNum_types:
        ty = proNum_type.Project_type
        if ty not in types:
            proNUMtype.append(projects.filter(Project_type=ty).count())
            types.append(ty)

    proNum_regions = models.Project.objects.annotate(count=Count('Region'))
    Regions = [];
    proNUMregion = []
    for proNum_region in proNum_regions:
        st = str(proNum_region.Region).strip()
        if st not in Regions:
            Regions.append(st)
            proNUMregion.append(projects.filter(Region=st).count())

    proNum_status = models.Project.objects.annotate(count=Count('Current_status'))
    status = [];
    proNUMstatus = []
    for proNum_statu in proNum_status:
        st = str(proNum_statu.Current_status).strip()
        if st not in status and len(st) != 0 and st != 'None':
            status.append(st)
            proNUMstatus.append(projects.filter(Current_status=st).count())
    # print(status, proNUMstatus)

    # workload
    workloads = {};
    YQs = []
    objs = models.Workload.objects.all()
    for obj in objs:
        YQ = obj.Year + obj.Quarter
        if YQ not in YQs:
            workloads[YQ] = round(
                objs.filter(Quarter=obj.Quarter, Year=obj.Year).aggregate(Sum('Workload')).get('Workload__sum'))

    COGS_by_BU = models.Project.objects.values("BU").annotate(total_COGS=Sum("Additional_COGS")).all()
    COGS_by_BUs = []
    for i in COGS_by_BU:
        COGS_by_BUs.append(round(i['total_COGS']))
    # print(COGS_by_BU)
    return render(request, 'project_dashboard-dark.html', locals())


# 项目卡页面
class ProjectDetail(APIView):
    # permission_classes = AllowAny
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'project_card.html'

    def get(self, request, pk):
        card = get_object_or_404(CardInfo, pk=pk)
        serializer = CardInfoModelSerializer(card)
        return Response({"serializer": serializer, 'card': card})

    # def post(self, request, pk):
    #     project = get_object_or_404(Project, pk=pk)
    #     serializer = ProjectModelSerializer(project, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'project': project})
    #     serializer.save()
    #     return redirect('/ProMGT')


# Project_name


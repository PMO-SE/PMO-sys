from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from PM import models
from django.db.models import Sum, Count
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response

from PM_admin.serializers import ProjectModelSerializer
from .models import Project, Workload

#Project Dashboard入口
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

def homepage(request):
    return render(request, 'Homepage.html')

# 增加项目或者首次登陆
def proMGT(request):
    projects = models.Project.objects.all()
    return render(request, 'ProMGT.html', locals())

def workload_MGT(request):
    # workloads = models.Workload.objects.all()
    return render(request, 'workload_MGT.html', locals())


# 视图集(增删改查流程封装的)
class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()

class ProjectDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'project_card.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(project)
        return Response({"serializer": serializer, 'project': project})

    # def post(self, request, pk):
    #     project = get_object_or_404(Project, pk=pk)
    #     serializer = ProjectModelSerializer(project, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'project': project})
    #     serializer.save()
    #     return redirect('/ProMGT')

# # 删除项目
# def project_delete(request):
#     # 先判断发过来的是否是post请求
#     if request.method == "POST":
#         # 得到要删除的id列表
#         id = request.POST.get("id", None)
#         project_obj = Project.objects.get(id=id)
#         project_obj.delete()
#     # 删除成功返回显示页
#     return HttpResponse("balabala")
#
# # 修改项目
# def project_edit(request):
#     # 先判断发过来的是否是post请求
#     if request.method == "POST":
#         ID = request.POST.get("ID", None)
#         Region = request.POST.get("Region", None)
#         project_name = request.POST.get("Name", None)
#         leader = request.POST.get("Leader", None)
#         cluster = request.POST.get("Cluster", None)
#         BU = request.POST.get("BU", None)
#         Plant = request.POST.get("Plant", None)
#         type = request.POST.get("Type", None)
#         Current_stage = request.POST.get("Curr_stage", None)
#         COGS = request.POST.get("COGS", None)
#         PROD = request.POST.get("PROD", None)
#         CAPEX = request.POST.get("CAPEX", None)
#         Space = request.POST.get("Space", None)
#         print("要修改的项目名称是", ID, "Region", Region)
#         book_obj = Project.objects.get(id=ID)
#         book_obj.Region = Region
#         book_obj.Project_leader = leader
#         book_obj.Cluster = cluster
#         book_obj.BU = BU
#         book_obj.Plant = Plant
#         book_obj.Project_type = type
#         book_obj.Current_status = Current_stage
#         book_obj.Additional_COGS = COGS
#         book_obj.Productivity = PROD
#         book_obj.CAPEX = CAPEX
#         book_obj.Space_needed = Space
#         book_obj.save()
#         a={'a':1}
#         a= json.dumps(a)
#     return JsonResponse(a,safe=False)
#
# # 增加项目
# def project_add(request):
#     # 先判断发过来的是否是post请求
#     if request.method == "POST":
#         Region = request.POST.get("Region", None)
#         project_name = request.POST.get("Name", None)
#         leader = request.POST.get("Leader", None)
#         cluster = request.POST.get("Cluster", None)
#         BU = request.POST.get("BU", None)
#         Plant = request.POST.get("Plant", None)
#         type = request.POST.get("Type", None)
#         Current_stage = request.POST.get("Curr_stage", None)
#         COGS = request.POST.get("COGS", None)
#         PROD = request.POST.get("PROD", None)
#         CAPEX = request.POST.get("CAPEX", None)
#         Space = request.POST.get("Space", None)
#         obj = Project(Region=Region, Project_name=project_name, Project_leader=leader, Cluster=cluster,
#                       BU=BU, Project_type=type, Current_status=Current_stage,
#                       Additional_COGS=COGS, Productivity=PROD, CAPEX=CAPEX, Space_needed=Space)
#         obj.save()
#     projects = models.Project.objects.all()
#     return render(request, 'ProMGT.html', locals())

# 为了project card而设定的


#为了页面显示Workload而设定的
# class WorkloadDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'workload_MGT.html'
#
#     def get(self, request, pk):
#         workload = get_object_or_404(Workload, pk=pk)
#         serializer = WorkloadModelSerializer(workload)
#         return Response({"serializer": serializer, 'workload': workload})
#
#     def get(self, request):
#         workload = Workload()
#         serializer = WorkloadModelSerializer(workload)
#         return Response({"serializer": serializer, 'workload': workload})
#
#     def post(self, request, pk):
#         project = get_object_or_404(Project, pk=pk)
#         serializer = ProjectModelSerializer(project, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'project': project})
#         serializer.save()
#         return redirect('/ProMGT')


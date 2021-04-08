import os
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from PMO_sys.settings import STATICFILES_DIRS, MEDIA_ROOT
from .filters import ProjectFilter, CardInfoFilter
from .serializers import ProjectModelSerializer, WorkloadModelSerializer, CardInfoModelSerializer
from rest_framework.viewsets import ModelViewSet
from PM.models import Project, Workload, CardInfo
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .permissions import IsOwner


# 分页类
class MyPageNumber(PageNumberPagination):
    page_size = 10  # 每页显示多少条
    page_size_query_param = 'limit'  # URL中每页显示条数的参数
    page_query_param = 'page'  # URL中页码的参数
    max_page_size = None  # 最大页码数限制


class ProjectView(ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectModelSerializer
    pagination_class = MyPageNumber
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('id', 'Project_leader', 'Current_status', 'Project_type', 'Project_name')
    ordering_fields = ('id', 'Project_leader')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(owner=request.user)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            res = {
                "code": 20000,
                "data": {
                    "total": queryset.count(),
                    "items": serializer.data,
                },
            }
            return Response(res)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {
            "code": 20000,
            "data": serializer.data,
        }
        # headers = self.get_success_headers(serializer.data)
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        # self.pre_delete(obj)
        obj.delete()
        # self.post_delete(obj)
        res = {"code": 20000}
        return Response(res)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        self.object = self.get_object()
        serializer = self.get_serializer(self.object, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     self.pre_save(serializer.object)
        # except ValidationError as err:
        #     # full_clean on model instance may be called in pre_save,
        #     # so we have to handle eventual errors.
        #     return Response(err.message_dict, status=status.HTTP_400_BAD_REQUEST)

        # if self.object is None:
        #     self.object = serializer.save(force_insert=True)
        #     self.post_save(self.object, created=True)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        self.object = serializer.save(force_update=True)
        # self.post_save(self.object, created=False)
        res = {
            "code": 20000,
            "data": serializer.data,
        }
        return Response(res, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        res = {
            "code": 20000,
            "data": serializer.data,
        }
        return Response(res)


class CardInfoView(ModelViewSet):
    queryset = CardInfo.objects.all().order_by('id')
    serializer_class = CardInfoModelSerializer
    pagination_class = MyPageNumber
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = CardInfoFilter
    search_fields = ('id',)
    ordering_fields = ('id',)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            res = {
                "code": 20000,
                "data": {
                    "total": queryset.count(),
                    "items": serializer.data,
                },
            }
            return Response(res)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {
            "code": 20000,
            "data": serializer.data,
        }
        # headers = self.get_success_headers(serializer.data)
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        # self.pre_delete(obj)
        obj.delete()
        # self.post_delete(obj)
        res = {"code": 20000}
        return Response(res)

    def update(self, request, *args, **kwargs):
        # partial = kwargs.pop('partial', False)
        self.object = self.get_object()
        serializer = self.get_serializer(self.object, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     self.pre_save(serializer.object)
        # except ValidationError as err:
        #     # full_clean on model instance may be called in pre_save,
        #     # so we have to handle eventual errors.
        #     return Response(err.message_dict, status=status.HTTP_400_BAD_REQUEST)

        # if self.object is None:
        #     self.object = serializer.save(force_insert=True)
        #     self.post_save(self.object, created=True)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        self.object = serializer.save(force_update=True)
        # self.post_save(self.object, created=False)
        res = {
            "code": 20000,
            "data": serializer.data,
        }
        return Response(res, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        res = {
            "code": 20000,
            "data": serializer.data,
        }
        return Response(res)


class WorkloadView(ModelViewSet):
    serializer_class = WorkloadModelSerializer
    queryset = Workload.objects.all().order_by('id')
    pagination_class = MyPageNumber

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            res = {
                "code": 20000,
                "data": {
                    "total": queryset.count(),
                    "items": serializer.data,
                },
            }
            return Response(res)


class Uploadimage(APIView):
    def post(self, request, *args, **kwargs):
        pf = request.FILES['file']
        id = request.POST.get('id')
        obj = CardInfo.objects.get(id=id)
        obj.Picture = pf
        obj.save()
        path = os.path.join(MEDIA_ROOT, 'image\\' + pf.name)
        with open(path, 'wb') as f:
            f.write(pf.read())
            print("小文件上传完毕")
        res = {
            "code": 20000,
            "path": path
        }
        return Response(res)


class Distinct(APIView):

    def get(self, request):
        distinct_name = Project.objects.values_list('Project_name', flat=True)
        distinct_IPL = [item[0] for item in Project.Name_category]
        distinct_Cluster = [item[0] for item in Project.Cluster_category]
        distinct_BU = [BU[0] for BU in Project.BU_category]
        distinct_Lob = [Lob[0] for Lob in Project.Lob_category]
        distinct_Plant = [item[0] for item in Project.Plant_category]
        distinct_Current_status = [item[0] for item in Project.Status_category]
        distinct_type = [item[0] for item in Project.Type_category]
        data = {
            'distinct_name': list(set(distinct_name)),
            'distinct_IPL': list(set(distinct_IPL)),
            'distinct_Cluster': list(set(distinct_Cluster)),
            'distinct_BU': list(set(distinct_BU)),
            'distinct_Lob': list(set(distinct_Lob)),
            'distinct_Plant': list(set(distinct_Plant)),
            'distinct_Current_status': list(set(distinct_Current_status)),
            'distinct_type': list(set(distinct_type)),
        }
        res = {
            'code': 20000,
            'data': data
        }
        return Response(res)

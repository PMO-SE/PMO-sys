from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .filters import ProjectFilter
from .serializers import ProjectModelSerializer, WorkloadModelSerializer, CardInfoModelSerializer
from rest_framework.viewsets import ModelViewSet
from PM.models import Project, Workload, CardInfo
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


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
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = ProjectFilter
    search_fields = ('id', 'Project_leader', 'Current_status', 'Project_type', 'Project_name')
    ordering_fields = ('id', 'Project_leader')

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
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = ProjectFilter
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

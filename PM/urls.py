from django.conf.urls import url
from . import modelView

urlpatterns = []

#drf中的路由
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('projects', modelView.ProjectModelViewSet, basename='projects')
urlpatterns += router.urls
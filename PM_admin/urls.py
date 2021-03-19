from django.urls import path
from rest_framework.routers import DefaultRouter  # drf中的路由
from .views import ProjectView, WorkloadView, CardInfoView

urlpatterns = [
    # path('', ProjectView.as_view({'get': 'list', 'post': 'create'})),

]
router = DefaultRouter()
router.register('project', ProjectView)
router.register('workload', WorkloadView)
router.register('card', CardInfoView)
urlpatterns += router.urls

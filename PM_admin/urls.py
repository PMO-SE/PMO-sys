from django.urls import path
from rest_framework.routers import DefaultRouter  # drf中的路由
from .views import ProjectView, WorkloadView, CardInfoView, Uploadimage, Distinct

urlpatterns = [
    # path('', ProjectView.as_view({'get': 'list', 'post': 'create'})),
    path('upload/image/', Uploadimage.as_view()),
    path('search_list/', Distinct.as_view())
]
router = DefaultRouter()
router.register('project', ProjectView)
router.register('workload', WorkloadView)
router.register('card', CardInfoView)
urlpatterns += router.urls

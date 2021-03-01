from django.urls import path
from rest_framework.routers import DefaultRouter  # drf中的路由
from .views import ProjectView

urlpatterns = [
    # path('', ProjectView.as_view({'get': 'list', 'post': 'create'})),

]
router = DefaultRouter()
router.register('', ProjectView)
urlpatterns += router.urls
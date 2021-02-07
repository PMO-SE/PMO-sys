from django.conf.urls import url
from . import modelView
from PM import views as PM_views
from django.urls import path

urlpatterns = [
    path('delete_project/', PM_views.project_delete),
    path('edit_project/', PM_views.project_edit),
    path('add_project/', PM_views.project_add),
    path('', PM_views.proMGT, name='proMGT'),
    path('project_card/pk', PM_views.proMGT),

]

# drf中的路由
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('projects', modelView.ProjectModelViewSet, basename='projects')
urlpatterns += router.urls

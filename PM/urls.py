from rest_framework.routers import DefaultRouter
from PM import views as PM_views
from django.urls import path

urlpatterns = [
    # path('delete_project/', PM_views.project_delete),
    # path('edit_project/', PM_views.project_edit),
    # path('add_project/', PM_views.project_add),
    path('', PM_views.proMGT, name='ProMGT'),
    path('project_dashboard/', PM_views.project_dashboard, name='project_dashboard'),
    path('project_card/<pk>/', PM_views.ProjectDetail.as_view(), name='project_card'),

]

router = DefaultRouter()
router.register('project', PM_views.ProjectModelViewSet)
urlpatterns += router.urls
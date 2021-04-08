from rest_framework.routers import DefaultRouter
from PM import views as PM_views
from django.urls import path

urlpatterns = [
    path('project_dashboard/', PM_views.project_dashboard, name='project_dashboard'),
    path('project_card/<pk>/', PM_views.ProjectDetail.as_view(), name='project_card'),

]

"""PMO_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PM import views as PM_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_dashboard', PM_views.project_dashboard, name='project_dashboard'),
    path('homepage/', PM_views.homepage, name='homepage'),
    path('proMGT/', PM_views.proMGT, name='proMGT'),
    path('project_card/', PM_views.project_card, name='project_card'),
    path('proMGT/delete_project/', PM_views.project_delete),
    path('proMGT/edit_project/', PM_views.project_edit),
    path('proMGT/add_project/', PM_views.project_add),

]

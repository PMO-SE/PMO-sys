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
from django.urls import path, include
from PM import views as PM_views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter  # drf中的路由

urlpatterns = [
    # -----------以下是前台使用的路由----------------------
    path('admin/', admin.site.urls),
    path('', PM_views.homepage),
    path('homepage/', PM_views.homepage, name='homepage'),
    path('ProMGT/', include('PM.urls')),  # 应用PM中的路由
    path('docs/', include_docs_urls(title='PMO sys API')),
    # ----------------以下是后台使用的路由------------------------
    # path('dev-api/project/', include('PM.admin-urls')),  # PM模块路由
    path('dev-api/project/', include('PM_admin.urls')),
    path('dev-api/vue-element-admin/user/', include('login.urls')),  # 登录login模块路由
    path('dev-api/vue-element-admin/', include('roles.urls'))

]
router = DefaultRouter()
# 前台路由
# router.register('project', modelView.ProjectModelViewSet, basename='projects')
# router.register('workloads', modelView.WorkloadModelViewSet, basename='workloads')
urlpatterns += router.urls

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from PM import views as PM_views
from rest_framework.documentation import include_docs_urls
from PMO_sys import settings

urlpatterns = [
    # -----------以下是前台使用的路由----------------------
    path('admin/', admin.site.urls),
    path('', PM_views.homepage),
    path('homepage/', PM_views.homepage, name='homepage'),
    path('ProMGT/', include('PM.urls')),  # 应用PM中的路由
    path('docs/', include_docs_urls(title='PMO sys API')),
    # ----------------以下是后台使用的路由------------------------
    path('dev-api/', include('PM_admin.urls')),
    path('dev-api/user/', include('login.urls')),  # 登录login模块路由
    path('dev-api/vue-element-admin/', include('roles.urls')),

    # 上传图片
    re_path('^dev-api/upload/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


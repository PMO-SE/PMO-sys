from django.urls import path
from . import views

urlpatterns = [
    path('roles', views.rolesView.as_view()),
    path('routes', views.routesView.as_view())
]
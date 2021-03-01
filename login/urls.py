from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginView.as_view()),
    path('info', views.userInfoView.as_view()),
    path('logout', views.logoutView.as_view())
]

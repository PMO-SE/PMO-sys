from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.TokenObtainPairView.as_view()),
    path('info/', views.userInfoView.as_view()),
    path('logout/', views.logoutView.as_view()),
    path('token/refresh/', views.TokenRefreshView.as_view()),
]

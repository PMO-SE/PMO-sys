from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', views.loginView.as_view()),
    # path('login/', obtain_jwt_token),
    path('info/', views.userInfoView.as_view()),
    path('logout/', views.logoutView.as_view())
]

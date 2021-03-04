from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from data.views import HomeView, user_login, user_logout, user_register, DetailCowView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path('cow/<slug:cow_name>/', DetailCowView.as_view(), name='DetailCow'),
    path('login/', user_login, name='MyLogin'),
    path('loginout/', user_logout, name='MyLogout'),
    path('register/', user_register, name='MyRegister'),
]

from django.urls import path
from . import views


urlpatterns = [

    #Authentication URLs
    path('register/', views.RegisterView, name="register"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('profile/', views.ProfileView, name="profile")
]
from .views import LoginView, RegisterationView, TestView
from django.urls import path


urlpatterns =[
    path("login/", LoginView.as_view(), name="login_user"),
    path("register/", RegisterationView.as_view(), name="login_user"),
    path("test/", TestView.as_view(), name="login_user"),

]
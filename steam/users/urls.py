from django.urls import path
from . import views
from users.forms import UserAuthentication
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('register/', views.register, name="reg"),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=UserAuthentication), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/exit.html'), name='logout'),
]
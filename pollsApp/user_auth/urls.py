# import liabraries
from django.urls import path
from . import views

# creating url patterns 
app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('login_view/', views.login_view, name='login_view'),
    path('register_view/', views.register_view, name='register_view'),
    path('logout/', views.logout_view, name='logout'),
]

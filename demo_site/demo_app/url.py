from django.urls import path
from . import views

app_name = 'demo_app'

urlpatterns = [
    path('', views.home,name = 'home'),
    path('add', views.add,name = 'add'),
    path('register', views.register, name='resister'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout')
]
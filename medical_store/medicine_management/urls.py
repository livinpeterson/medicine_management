from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signuppage, name='signup'),
    path('', views.loginpage, name='login'),
    path('index', views.index, name='index'),
    path('search', views.searchpage, name='search'),
    path('add', views.create, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('logout', views.logoutpage, name='logout'),
    
]
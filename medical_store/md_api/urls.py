from django.urls import path
from md_api import views

urlpatterns = [
    path('signupmedi', views.signup_medi, name='signupmedi'),
    path('loginmedi', views.login_medi, name='loginmedi'),
    path('listmedi', views.list_medi, name='listmedi'),
    path('searchmedi/<str:name>', views.search_medi, name='searchmedi'),
    path('createmedi', views.create_medi, name='createmedi'),
    path('updatemedi/<int:id>', views.update_medi, name='updatemedi'),
    path('deletemedi/<int:id>', views.delete_medi, name='deletemedi'),
]
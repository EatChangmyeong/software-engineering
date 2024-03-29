from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_request/', views.login_request, name='login_request'),
    path('register/', views.register, name='register'),
    path('register_request/', views.register_request, name='register_request'),
    path('user/', views.user_page, name='user_page'),
    path('user_edit/', views.user_edit, name='user_edit'),
    path('user_edit_request/', views.user_edit_request, name='user_edit_request'),
    path('logout/', views.logout, name='logout'),
]
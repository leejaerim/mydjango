from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserView
from .models import User
from . import views

user_list = UserView.as_view({
    'post':'create',
    'get':'list'
})
user_detail = UserView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.login, name = 'login'),
    path('signup/',views.signup,name='signup'),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
])
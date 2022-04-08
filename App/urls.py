from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserView, MenuOrderView, PostView
from .models import User,MenuOrder
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
post_list = PostView.as_view({
    'post':'create',
    'get':'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
Menu_OrderView = MenuOrderView.as_view({
    'get':'list',
    'post':'create'
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.login, name = 'login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('post/',views.PostlistView,name='PostListView'),
    path('post/<int:pk>/',views.getPostView,name='getPostView'),
    path('order/',views.order,name='order'),
    path('menucount/',Menu_OrderView,name='Menu_OrderView'),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
])
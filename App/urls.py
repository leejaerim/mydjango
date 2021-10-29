from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserView

user_list = UserView.as_view({
    'post':'create',
    'get':'list'
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', user_list, name='user_list'),
    #path('posts/<int:pk>/', post_detail, name='post_detail'),
])
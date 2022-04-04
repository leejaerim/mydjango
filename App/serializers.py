from rest_framework import serializers
from .models import Post, User
from .models import MenuOrder
#from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','uid', 'password')

class MenuOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOrder
        fields =  ('sumCost','regDate')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','text','author','create_at')
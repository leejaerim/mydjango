from rest_framework import viewsets
from rest_framework.decorators import permission_classes
import json
from rest_framework.serializers import Serializer
from .serializers import UserSerializer
from .models import User
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
def login(request):
    # if request.method == 'GET':
    #     users = User.objects.all().order_by('-uid')
    #     return render(request, {'user':users})
    if request.method =='POST':
        uid = request.POST['uid']
        password = request.POST['password']
        data = {}
        user = User.objects.get(uid = uid)
        if check_password(password, user.password):
            return redirect('game/')
        else:
            data['Error'] = '비밀번호가 틀렸습니다.'
    return HttpResponse(data)
def signup(request):
    data = {}
    body = json.loads(request.body)
    if request.method  == 'POST':
        if User.objects.filter(uid=body['uid']).exists(): 
            data['Error'] = '이미 존재하는 사용자 입니다.'
            return HttpResponse(data)
        elif body['uid'] is None or body['password'] is None:
            data['Error'] = '정보를 정확히 입력하세요.'
            return HttpResponse(data)
        else:
            user = User(
                uid = body['uid'],
                password = body['password']
            )
            user.save()
            #auth.login(request, user)
            data['status'] = True
            return HttpResponse(data)
    return redirect('Join')
@method_decorator(csrf_exempt,name='dispatch')
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
        #serializer.save(user=self.request.user)

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
from django.contrib.auth.hashers import check_password, make_password
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./django-fae27-firebase-adminsdk-uvgy6-04d6add42a.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://django-fae27-default-rtdb.firebaseio.com/'
})
def login(request):
    # if request.method == 'GET':
    #     users = User.objects.all().order_by('-uid')
    #     return render(request, {'user':users})
    if request.method =='POST':
        body = json.loads(request.body)
        uid = body['uid']
        password = body['password']
        data = {}
        if User.objects.filter(uid=uid).exists():
            user = User.objects.get(uid = uid)
            if check_password(password, user.password):
                dir = db.reference('history')
                dir.update({'login':user.uid})
                request.session['user'] = user.uid
                data['status'] = 'Success'
            else:
                data['Error'] = '비밀번호가 틀렸습니다.'
        else:
            data['Error'] = '없는 아이디 입니다.'
    return HttpResponse(json.dumps(data), content_type="application/json")
def signup(request):
    data = {}
    body = json.loads(request.body)
    if request.method  == 'POST':
        if User.objects.filter(uid=body['uid']).exists(): 
            data['Error'] = '이미 존재하는 사용자 입니다.'
        else:
            user = User(
                uid = body['uid'],
                password = make_password(body['password'])
            )
            user.save()
            #auth.login(request, user)
            data['status'] = 'Success'
        return HttpResponse(json.dumps(data), content_type="application/json")
def logout(request):
    data = {}
    if request.session.get('user'):
        del(request.session['user'])
        data['status'] = 'Success'
    else:
        data['Error'] = '정보를 정확히 입력하세요.'
    return HttpResponse(json.dumps(data), content_type="application/json")    
        
@method_decorator(csrf_exempt,name='dispatch')
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
        #serializer.save(user=self.request.user)

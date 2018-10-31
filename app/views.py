import hashlib
import random
import time
import uuid

from django.http import HttpResponse, response
from django.shortcuts import render, redirect


# Create your views here.
from app.models import User


def index(request):

    # 状态保持 —— 获取 session
    # username = request.session.get('username')




    # 状态保持 - 获取token
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)
    if users.exists():
        user = users.first()
        return render(request, 'index.html', context={'username': user.username})
    else:
        return render(request, 'index.html')
    #
    #
    # return render(request,'index.html',context={'username':username})
def generate_token():
    token = str(time.time())  + str(random.random())

    # MD5
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()

def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

def detail(request):
    return render(request,'html/detail.html')


def list(request):
    return render(request,'html/list.html')


def login(request):
    if request.method == "GET":
        return render(request,'html/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password =  generate_password( request.POST.get("password") )
        # print(username,password)

        users = User.objects.filter(username=username).filter(password=password)

        if users.exists():

            user = users.first()

            #token
            user.token = generate_token()
            user.save()

            response = redirect('leshangwang:index')

            # 状态保持 - token
            response.set_cookie('token', user.token)

            return response
        else:
            return HttpResponse('用户名或密码错误!')


def register(request):
    if request.method ==  "GET":
        return render(request,'html/register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        #存入数据库
        try:
            user = User()
            user.username = username
            user.password = generate_password(password)

            user.token = uuid.uuid5(uuid.uuid4(),'register')

            user.save()

            #
            response = redirect('leshangwang:index')

            # 状态保持 - token
            response.set_cookie('token', user.token)

            return response
        except Exception as e:
            return HttpResponse('注册失败' + e)



def shoppingCar(request):
    return render(request,'html/shoppingCar.html')
import hashlib
import random
import time
import uuid

from django.http import HttpResponse, response
from django.shortcuts import render, redirect


# Create your views here.
from app.models import User, goods


def index(request):
    username = request.COOKIES.get('username')
    data = {
        'username':username,
    }
    return render(request,'index.html',context=data)

#token生成
def generate_token():
    token = str(time.time())  + str(random.random())

    # MD5
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()

#加密
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

def detail(request):
    return render(request,'html/detail.html')


def list(request):
    wheels = goods.objects.all()

    data = {
        'wheels':'wheels',
    }

    return render(request,'html/list.html',context=data)


def login(request):
    if request.method == "GET":
        return render(request,'html/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password =  generate_password( request.POST.get("password") )
        print(username,password)

        users = User.objects.all().filter(username=username).filter(password=password)
        if users.exists():
            user = users[0]
            response = redirect('leshangwang:index')
            response.set_cookie('username', user.username)
            print(username)
            return response
        else:
            return HttpResponse('用户名或密码错误!')


def register(request):
    if request.method ==  "GET":
        return render(request,'html/register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('username')
        print(username,password,tel)

        #存入数据库
        try:
            user = User()
            user.username = username
            user.password = generate_password(password)
            user.tel = username
            user.save()    #
            response = redirect('leshangwang:index')
            response.set_cookie('username', user.username)
            return response
        except Exception as e:
            return HttpResponse('注册失败' + e)



def shoppingCar(request):
    username = request.COOKIES.get('username')
    return render(request,'html/shoppingCar.html',context={'username':username})


def logout(request):
    response = redirect('leshangwang:index')
    response.delete_cookie('username')
    return response


def mine(request):
    return render(request,'html/mine.html')
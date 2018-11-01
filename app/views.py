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

    #状态保持 —— 获取 cookies
    # username = request.COOKIES.get('username')


    # 状态保持 - 获取token
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)
    if users.exists():
        user = users.first()
        return render(request, 'index.html', context={'username':user.username})
    else:
        return render(request, 'index.html')
    #
    # session和cookie返回
    # return render(request,'index.html',context={'username':username})

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

            # 状态保持 - 设置cookie
            # 状态保持 - 设置session
            # request.session['username'] = username
            # request.session.set_expiry(60)

            #token
            user.token = generate_token()
            user.save()

            response = redirect('leshangwang:index')

            # 状态保持 - cookie
            # response.set_cookie('username', username)

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
        tel = request.POST.get('username')
        print(username,password,tel)

        #存入数据库
        try:
            user = User()
            user.username = username
            user.password = generate_password(password)
            user.tel = username

            #token生成
            # 随机数
            # 时间戳 + 随机数
            # 时间戳 + 随机数 + 公司 + IP
            # user.token = generate_token()

            # 系统提供
            # uuid.uuid1() # 基于时间戳(不建议使用)
            # uuid.uuid2()  # 基于分布式计算环境(python没有)
            # uuid.uuid3()  # 基于名字的md5离散值 [推荐使用]
            # uuid.uuid4()  # 基于随机数(不建议使用)
            # uuid.uuid5()  # 基于名字的SHA-1离散值 [推荐使用]
            user.token = uuid.uuid5(uuid.uuid4(), user.username)
            # user.token = uuid.uuid5(uuid.uuid4(),'register')

            user.save()

            #
            response = redirect('leshangwang:index')

            # 状态保持 - 设置cookie
            # 状态保持 - 设置session   【base64】
            # ZGRkODZmNjkyMzc2M2MyYWFiMWNjMmNlZjBhZTRmNjM3MDNhMjJiNjp7InVzZXJuYW1lIjoicXEifQ==
            # request.session['username'] = username
            # request.session.set_expiry(60)

            # 状态保持 - token
            response.set_cookie('token', user.token)

            return response
        except Exception as e:
            return HttpResponse('注册失败' + e)



def shoppingCar(request):
    username = request.COOKIES.get('username')

    return render(request,'html/shoppingCar.html',context={'username':username})





def logout(request):
    response = redirect('leshangwang:index:index')

    ## session
    # 方式一: session是借助于cookie
    # response.delete_cookie('sessionid')

    # 方式二: 直接删除session存储
    # del request.session['username']

    # 方式三: 同时删除cookie和session
    # request.session.flush()

    # response.delete_cookie('username')

    # token
    response.delete_cookie('token')

    return response



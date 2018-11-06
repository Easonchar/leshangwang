from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^index/$',views.index,name='index'),
    # url(r'^home/$',views.home,name='home'),

    url(r'^detail/$',views.detail,name='detail'),
    url(r'^list/$',views.list,name='list'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$,',views.logout,name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^shoppingCar/$',views.shoppingCar,name='shoppingCar'),
    url(r'^mine/$',views.mine,name='mine'),



]
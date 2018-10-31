from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^index/$',views.index,name='index'),
    url(r'^detail(\d+)/$',views.detail,name='detail'),
    url(r'^list/$',views.list,name='list'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^shoppingCar/$',views.shoppingCar,name='shoppingCar'),


]
from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin
#from django.contrib.auth import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'shop'

urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),

    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),

    url(r'^product_list/$', views.product_list, name='product_list'),
    url(r'^product_detail/$', views.product_detail, name='product_detail'),

]

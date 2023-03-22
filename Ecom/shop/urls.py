
from django.contrib import admin
from . import views
from django.urls import path
app_name='shop'

urlpatterns=[
    # path('',views.index,name='index'),
    path('', views.allProdCart, name='allProdCart'),
    path('<slug:c_slug>/', views.allProdCart, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]
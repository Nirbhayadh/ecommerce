from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('', views.getRoutes, name='routes'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>', views.getProduct, name='product'),

]
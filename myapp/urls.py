from django.contrib import admin

from django.urls import path

from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
    path('', views.hello, name='home'),
    path('products', views.products, name='products'),
    path('home/', views.home, name='home'),
    path('organic/', views.organic, name='organic'),


]

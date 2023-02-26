from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your URL patterns here ...
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='home'),
    path('products', views.products, name='products'),
    path('home/', views.home, name='home'),
    path('organic/', views.organic, name='organic'),

]

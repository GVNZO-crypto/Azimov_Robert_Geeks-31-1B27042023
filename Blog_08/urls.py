"""
URL configuration for Blog_08 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
# from posts import views
from Product import views as product_views
from users import views as users_views
from Blog_08 import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # Первая домашка
    # path('', views.test_view),
    # path ('hello/', views.hello_views),
    # path ('time/', views.time),
    # path ('goodbye/', views.goodbye),
    path('', product_views.main_view,name='index'),
    path('products/', product_views.product_view,name='products'),
    path('product/<int:id>/', product_views.product_detail_view,name='product_detail_view'),
    path('category/', product_views.category,name='category'),
   
    path('products/create', product_views.create_product),
    path('category/create', product_views.create_category),
    
    path('users/register', users_views.register_view),
    path('users/auth', users_views.auth_view),
    path('users/logout', users_views.logout_view),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from electron import views

urlpatterns = [
    # index page
    url(r'^$', views.index, name='index'),
    # products page
    url(r'^products$', views.products, name='products'),
    # products by category
    url(r'^products/(?P<category>[\w ]+)$', views.products_category, name='products_category'),
    # individual product
    url(r'^products/product/(?P<id>[\d]+)$', views.individual_product, name='individual_product'),
    # register page
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # login page
    url(r'^login/$', auth_views.login, name='login'),
    # logout page
    url(r'^logout/$', auth_views.logout, name='logout'),
    # admin
    url(r'^admin/', admin.site.urls),
]

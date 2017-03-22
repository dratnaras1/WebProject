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
from electron import views, basket_controller
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
    url(r'^login/$', views.login_user, name='login'),
    # logout page
    url(r'^logout/$', auth_views.logout, name='logout'),
    # add item to basket
    url(r'^add/(?P<id>[\d]+)/$', basket_controller.add_to_basket, name='add-to-basket'),
    # show basket
    url(r'^shopping-basket/$', views.show_basket, name='show-basket'),
    # empty basket
    url(r'^empty-basket/$', basket_controller.empty_basket, name='empty-basket'),
    # delete item from basket
    url(r'^delete-item/(?P<id>[\d]+)/$', basket_controller.delete_item, name='delete-item'),
    # admin
    url(r'^admin/', admin.site.urls),
]


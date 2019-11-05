"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import member.api
import order_list.api
import my_cash.api
import auto_policy.api
import balance_check.api
import activity_check.api

from balance_check.views import BalanceCheck

from order_list import views



app_name='member'
router = routers.DefaultRouter()
router.register('members', member.api.MemberViewSet)

list_name = 'order_list'
router.register('order_list', order_list.api.OrderListViewSet)

mycash_name = 'my_cash'
router.register('my_cash', my_cash.api.MyCashViewSet)

auto_policy_name = 'auto_policy'
router.register('auto_policy', auto_policy.api.AutoPolicyViewSet)

balance_check_name = 'balance_check'
router.register('balance_check', balance_check.api.BalanceCheckViewSet)

activity_check_name = 'activity_check'
router.register('activity_check', activity_check.api.ActivityCheckViewSet)


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path(r'api/doc', get_swagger_view(title='Rest API Document')),
    path(r'api/v1/', include((router.urls, 'member'), namespace='api')),
    path(r'api/v1/', include((router.urls, 'order_list'), namespace='api')),
    path(r'api/v1/', include((router.urls, 'my_cash'), namespace='api')),
    path(r'api/v1/', include((router.urls, 'auto_policy'), namespace='api')),
    path(r'api/v1/', include((router.urls, 'balance_check'), namespace='api')),
    path(r'api/v1/', include((router.urls, 'activity_check'), namespace='api')),
    #path(r'api/v1/^(P?<pk>[0-9]+)/$', views.order_list),
]

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from api import views

urlpatterns = [
    # 设备请求的url
    path('getstate', views.get_device_status),
    path('getconfig', views.get_config),
    
    # 编辑配置信息的url
    path('state_list/', views.DeviceStatusList.as_view()),
    path('add_edit_config/', views.AddEditConfig.as_view()),
    path('delete_config/', views.DeleteConfig.as_view()),
    path('admin/', admin.site.urls),
    re_path('', views.DeviceList.as_view()),
]

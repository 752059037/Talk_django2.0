from django.shortcuts import render, redirect, HttpResponse
from api import models
from api.utils import is_ascii
from api.forms import DeviceConfigForm, DeviceStatusForm
from django import views
import logging
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
import datetime

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt=' %Y-%m-%d %H:%M:%S',
                    filename='bug.log', filemode='a',
                    )


@csrf_exempt  # 取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
@api_view(http_method_names=['post', 'get'])  # 只允许post
@permission_classes((permissions.AllowAny,))  # 允许任意人发送rest请求
def get_config(request):
    try:
        device_id = request.GET.get('deviceID', '')  # 获取设备ID
        if len(device_id) == 16 and is_ascii(device_id):  # 设备ID为16位ASCII字符
            device_obj = models.DeviceConfig.objects.filter(device_id=device_id).values().first()
            if device_obj:
                return Response(device_obj)
        else:
            return HttpResponse("ERROR:device_id does not exist")
    except Exception as get_config_error:
        logging.error(get_config_error)


@csrf_exempt  # 取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
@api_view(http_method_names=['post', 'get'])  # 只允许post
@permission_classes((permissions.AllowAny,))  # 允许任意人发送rest请求
def get_device_status(request):
    """
    接收设备心跳信息
    :param request:
    :return:
    """
    try:
        device_id = request.GET.get('deviceID', '')
        powersupply = request.GET.get('power_supply', '')
        network = request.GET.get('net_work', '')
        devicetime = request.GET.get('devicetime', '')
        storage = request.GET.get('storage', '')
        wifi_db = request.GET.get('wifi_db', '')
        insertime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间：
        if len(device_id) == 16 and is_ascii(device_id):
            if powersupply in ['0', '1'] and network in ['0', '1'] and devicetime.isdigit() and storage.isdigit():
                devicetime = datetime.datetime.fromtimestamp(int(devicetime))
                data = {'device_id': device_id,
                        'powersupply': powersupply,
                        'network': network,
                        'devicetime': devicetime,
                        'storage': storage,
                        'insertime': insertime,
                        'wifi_db': wifi_db
                        }
                form_obj = DeviceStatusForm(data)
                if form_obj.is_valid():
                    form_obj.save()
                    return HttpResponse("OK")
                else:
                    return HttpResponse("ERROR:Data check failed")
            else:
                return HttpResponse("ERROR:Parameters do not conform to the rules")
        else:
            return HttpResponse("ERROR:device_id does not exist")
    except Exception as get_heartbeat_error:
        logging.error(get_heartbeat_error)


class DeviceStatusList(views.View):
    @staticmethod
    def get(request):
        device_id = request.GET.get('deviceID', '')
        query_dict = models.DeviceStatus.objects.filter(device_id=device_id).values()
        status_list = list(query_dict)
        return render(request, 'state_list.html', {'status_list': status_list, 'device_id':device_id})


class DeviceList(views.View):  # 显示设备列表
    @staticmethod
    def get(request):
        device_id_list = models.DeviceConfig.objects.values_list('device_id')
        device_id_list = [i[0] for i in device_id_list]
        return render(request, 'device_list.html', {'device_id_list': device_id_list})


class AddEditConfig(views.View):  # 添加/编辑配置
    @staticmethod
    def get(request):
        device_id = request.GET.get('deviceID', '')
        config_obj = models.DeviceConfig.objects.filter(device_id=device_id).first()
        form_obj = DeviceConfigForm(instance=config_obj)
        return render(request, 'add_edit_config.html', {'form_obj': form_obj, 'device_id': device_id})
    
    try:
        @staticmethod
        def post(request):
            device_id = request.GET.get('deviceID', '')
            config_obj = models.DeviceConfig.objects.filter(device_id=device_id).first()
            form_obj = DeviceConfigForm(request.POST, instance=config_obj)
            if form_obj.is_valid():
                form_obj.save()
                _next_url = '/'
                return redirect(_next_url)
            else:
                return render(request, 'add_edit_config.html', {
                    'form_obj': form_obj,
                    'device_id': device_id,
                    'error_msg': form_obj.errors
                })
    except Exception as save_config_error:
        logging.error(save_config_error)
        
class DeleteConfig(views.View):
    @staticmethod
    def get(request):
        device_id = request.GET.get('deviceID', '')
        form_obj = models.DeviceConfig.objects.filter(device_id=device_id).first()
        form_obj.delete()
        return redirect('/')
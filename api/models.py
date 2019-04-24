from django.db import models


# Create your models here.

class DeviceConfig(models.Model):
    device_id = models.CharField(max_length=255, unique=True)
    heart_interval = models.IntegerField(default=60)
    work_time_start = models.CharField(max_length=255)
    work_time_end = models.CharField(max_length=255)
    record_start = models.IntegerField()
    record_end = models.IntegerField()
    file_max_len = models.IntegerField(default=2)
    upload_ftp_address = models.CharField(max_length=255)
    upload_ftp_passwd = models.CharField(max_length=255)
    upload_ftp_usr = models.CharField(max_length=255)
    upload_ftp_path = models.CharField(max_length=255)
    update_ftp_address = models.CharField(max_length=255)
    update_ftp_passwd = models.CharField(max_length=255)
    update_ftp_path = models.CharField(max_length=255)
    soft_ver = models.CharField(max_length=255)
    ntpserver = models.CharField(max_length=255)
    uploadfile_time = models.IntegerField()
    config_interval = models.IntegerField(default=720)
    wifi_ssid = models.CharField(max_length=16)
    wifi_psword = models.CharField(max_length=16)
    start_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    

class DeviceStatus(models.Model):
    device_id = models.CharField(max_length=16)
    powersupply = models.CharField(max_length=1)
    network = models.CharField(max_length=1)
    devicetime = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    wifi_db = models.CharField(max_length=255)
    start_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    

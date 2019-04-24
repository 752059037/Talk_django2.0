from django.db import models


# Create your models here.


class DeviceConfig(models.Model):
    record_start_choice = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    device_id = models.CharField(max_length=16, unique=True,
                                 help_text="字符串	16 位ASSCII码设备ID。第一批设备序列号： TK2019040001-TK2019040200 "
    
                                 )
    heart_interval = models.IntegerField(
        default=10, help_text='整数	默认10分钟'
    )
    work_time_start = models.CharField(max_length=255, help_text='字符串	设备开始工作时间	09:00')
    work_time_end = models.CharField(max_length=255, help_text='字符串	设备工作结束时间	18:00')
    record_start = models.IntegerField(default=1, help_text='整数	1-5 ，默认1', choices=record_start_choice)
    record_end = models.IntegerField(default=10, help_text='整数	10-60 秒 ，默认10秒')
    file_max_len = models.IntegerField(default=4, help_text='整数	录音文件最大长度,单位MB，最大100默认4')
    upload_ftp_address = models.CharField(max_length=255, default='talktrack.cfss-auto-dealer.cn',
                                          help_text='字符串	47.97.71.185	'
                                          )
    upload_ftp_passwd = models.CharField(max_length=255, help_text='字符串	20141101')
    upload_ftp_usr = models.CharField(max_length=255, help_text='字符串	uftp')
    upload_ftp_path = models.CharField(
        max_length=255,
        help_text='	字符串	一级目录：talktrack ，二级目录对应设备序列号后六位（040001-040200 ）序列号 TK2019040001对应目录  talktrack\040001')
    update_ftp_address = models.CharField(max_length=255, help_text='字符串	talktrack.cfss-auto-dealer.cn')
    update_ftp_passwd = models.CharField(max_length=255, help_text='字符串	uftp')
    update_ftp_path = models.CharField(max_length=255, help_text='字符串	system_file')
    soft_ver = models.CharField(max_length=255, help_text='字符串	设备固件软件版本号，设备根据固件版本号判断是否需要升级')
    ntpserver = models.CharField(max_length=255, default='ntp1.aliyun.com,ntp2.aliyun.com',
                                 help_text='字符串	NTP服务器域名	ntp1.aliyun.com,ntp2.aliyun.com')
    uploadfile_time = models.IntegerField(default=0, help_text='整数	录音文件定时上传时间间隔，单位分钟.默认0代表立刻录音完成马上传')
    config_interval = models.IntegerField(default=5, help_text='整数	配置参数查询间隔，单位分钟，默认5')
    wifi_ssid = models.CharField(max_length=16, default='jetson', help_text='字符串	 jetson')
    wifi_psword = models.CharField(max_length=16, default='20141101', help_text='字符串	 20141101')
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

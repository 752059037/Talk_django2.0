# 创建人;Ye
# 创建时间 : 19.4.18  10:52

from api import models
from django import forms
from api.utils import is_ascii
from django.core.exceptions import ValidationError


class Foo(forms.ModelForm):
    def clean_device_id(self):  # 校验设备id是否为ASCII码组成
        if is_ascii(self.cleaned_data['device_id']):
            return self.cleaned_data['device_id']
        raise ValidationError('设备ID应为16位ASCII码')


class DeviceConfigForm(Foo):
    device_id = forms.CharField(min_length=16, max_length=16,
                                strip=True,  # 是否移除用户输入空白
                                error_messages={"required": "该字段不能为空",
                                                "min_length": "设备ID长度为十六位",
                                                "max_length": "设备ID长度为十六位"})
    
    class Meta:
        model = models.DeviceConfig
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            # import pdb
            # pdb.set_trace()
            i.widget.attrs.update({'class': 'input form-control'})


class DeviceStatusForm(Foo):
    class Meta:
        model = models.DeviceStatus
        fields = "__all__"
    
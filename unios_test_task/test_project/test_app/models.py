from django.db import models

class Device(models.Model):
    device_title = models.CharField(max_length=200)
    device_code = models.CharField(max_length=200)
    device_id = models.IntegerField(primary_key=True)
    device_time = models.DateTimeField(auto_now_add=True)

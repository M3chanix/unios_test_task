from rest_framework import serializers
from test_app.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['device_id', 'device_title', 'device_code', 'device_time']

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.device_title = validated_data.get('title', instance.title)
        instance.device_code = validated_data.get('code', instance.code)
        instance.save()
        return instance


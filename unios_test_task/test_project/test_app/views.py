from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from test_app.models import Device
from test_app.serializers import DeviceSerializer

def index(request):
    device_list = Device.objects.all()
    template = loader.get_template('test_app/index.html')
    context = {
        'device_list': device_list,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def device_list(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

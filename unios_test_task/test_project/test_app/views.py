from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from test_app.models import State
from test_app.serializers import StateSerializer
from django.contrib.auth.decorators import login_required
from test_app.forms import StateForm

#@login_required
def index(request):
    state_list = State.objects.all()
    template = loader.get_template('test_app/table.html')
    form = StateForm()
    context = {
        'state_list': state_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def state_list(request):
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        data = request.POST
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # вместо возврата значений обновить страницу
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def change(request, pk):
    try:
        state = State.objects.get(pk=pk)
    except State.DoesNotExist:
        return HttpResponse(status=404)

    data = request.PUT
    serializer = StateSerializer(state, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

    
def delete(request, pk):
    try:
        state = State.objects.get(pk=pk)
    except State.DoesNotExist:
        return HttpResponse(status=404)
    state.delete()
    return HttpResponse(status=204)


def authentification(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)


from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from test_app.models import State
from test_app.serializers import StateSerializer
from django.contrib.auth.decorators import login_required
from test_app.forms import StateForm
from django.forms import modelformset_factory, TextInput
from django.contrib.auth import authenticate

def index(request):
    #state_list = State.objects.all()
    template = loader.get_template('test_app/formset.html')
    StateFormSet = modelformset_factory(
            State, form=StateForm, extra=0)
    formset = StateFormSet()
    #formset.full_clean()
    #print(formset.is_valid())
    #print(formset.is_bound)
    context = {
        'formset': formset
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'test_app/formset.html', {'formset': formset})

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

@login_required
def edit(request, pk):
    StateFormSet = modelformset_factory(    
            State, form=StateForm,    
            extra=0)
    data = request.POST
    serializer = StateSerializer(data=data, many=True)
    if serializer.is_valid():
        formset = StateFormSet(serializer.validated_data)
    #if formset.is_valid():
        #cleanformset = formset.save(commit = False)
        #print(cleanformset)
        return render(request, 'test_app/formset.html', {'formset': formset})


def save(request, pk):
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


@login_required
def delete(request, pk):
    try:
        state = State.objects.get(pk=pk)
    except State.DoesNotExist:
        return HttpResponse(status=404)
    state.delete()
    return HttpResponse(status=204)


def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return HttpResponse("Invalid login-password pair.")

def login(request):
    return render(request, "test_app/login_form.html")

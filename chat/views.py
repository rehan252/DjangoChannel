# chat/views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return HttpResponse(room_name)

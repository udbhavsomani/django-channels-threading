from django.shortcuts import render
from django.http import JsonResponse
import json

from .thread import CreateStudentData


def home(request):
    return render(request, 'home.html')


def generate_data(request):
    count = int(request.GET.get('count'))
    CreateStudentData(count).start()
    return JsonResponse({'status': 200})

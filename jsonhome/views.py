from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def hello(request):
    json = {"Message": "Hello World!"}
    return JsonResponse(json)
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Wlcome to the main polls page")
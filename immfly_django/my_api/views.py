# from django.shortcuts import render

from django.http import HttpResponse

def TVSHOW(request):
    
    return HttpResponse("TV SHOW Page")
# Create your views here.

def AUDIBLE(request):
    
    return HttpResponse("AUDIBLE Page")

def MOVIES(request):
    
    return HttpResponse("MOVIES Page")

def LIFESTYLE(request):
    
    return HttpResponse("LIFESTYLE Page")

def MUSIC_PODCASTS(request):
    
    return HttpResponse("MUSIC AND PODCASTS Page")

def KIDS(request):
    
    return HttpResponse("KIDS Page")

def PRESS_MAGAZINES(request):
    
    return HttpResponse("PRESS AND MAGAZINES Page")

def GAMES(request):
    
    return HttpResponse("GAMES Page")


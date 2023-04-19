# from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    
    return HttpResponse("Hi, telita con el proyecto")

# from rest_framework import viewsets
# from .models import Book
# from .serializers import BookSerializer

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


#CRUD Operation
class ListTodo(generics.ListAPIView): #GET
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UpdateTodo(generics.RetrieveUpdateAPIView): #PUT
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView): #Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView): # Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
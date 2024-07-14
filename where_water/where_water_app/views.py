from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    #return HttpResponse("hello world!")
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def view_chat(request):
    return render(request, "chat/chat.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
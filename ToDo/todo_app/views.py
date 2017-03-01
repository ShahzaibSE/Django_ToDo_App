from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,Http404
from django.template import loader

#Import models
from .models import Tasks;

# Create your views here.
# def index(request):  #Method1
#     todos = Tasks.objects.all();
#     print("To-Dos");
#     print(todos);
#     template = loader.get_template('todo_app/index.html');
#
#     todos = {
#         'todos':todos
#     }
#
#     return HttpResponse(template.render(todos,request))
#
#
#     # render('templates/index.html',{'todos':todos});

def index(request): #Method2 -> shortcut
    todos = Tasks.objects.all();
    print("To-Dos");
    print(todos);
    template = loader.get_template('todo_app/index.html');

    todos = {
        'todos':todos
    }

    return render(request,'todo_app/index.html',todos);

def HelloWorld(request):

    obj = {'status':True,'message':"Hello World with Django"}

    return HttpResponse("Hello World with Django")
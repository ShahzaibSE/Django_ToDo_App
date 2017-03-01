from django.conf.urls import include,url

#Import Endpoints/Views
from . import views

urlpatterns = [
    url('index',views.index,name='index'),
    url('hello',views.HelloWorld,name='helloworld')
]
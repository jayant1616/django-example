from django.shortcuts import render
from django.http import HttpResponse
from hello.models import topics
from hello import forms
# Create your views here

def index(request):
    form_obj = forms.input_form()#created an objec
    dict_test={'tag':form_obj,}
    form_obj=forms.input_form(request.POST)

    model_obj = topics(topic_name=' ',topic_email= 't@gmail.com')



    return render(request,'hello/form.html',context =dict_test)
def users(request):

    return render(request,'hello/users.html',{'users':model_object,})

# Create your views here.
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
class Userform(forms.Form):
    name=forms.CharField(max_length=30)

def register(req):
    if req.method=='POST':
        form=Userform(req.POST)
        if form.is_valid():
            return HttpResponse('ok')
    else:
        form=Userform()
    return render_to_response('register.html',{'form':form})

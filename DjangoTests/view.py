from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import requests
def hello (request):
    context = {}
    context['hello'] = 'Hello World!'
    
    return render(request, 'hello.html', context)

def login(request):
    return render_to_response('OAuth.html')

def loginresult(request):
    request.encoding = 'utf-8'
    if ('username' in request.GET) and ('password' in request.GET):
        message = 'Login information:\n Username:' + request.GET['username'] + '\nPassword:' + request.GET['password']
        #url = 
    else:
        message = 'Login information not valid\n'
    
    return HttpResponse(message)


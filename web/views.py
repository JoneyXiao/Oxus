from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse

# Create your views here.

def login(request):
    return render_to_response('login.html')

def list(request, id1,id2):
    return HttpResponse(id1 + id2)

def get(request):
    userList = UserInfo.objects.all()
    result = render_to_response('user.html', {'userData':userList})
    return result
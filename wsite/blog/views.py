from django.shortcuts import render
import datetime

from django.http import HttpResponse
def helloworld(request):
    return HttpResponse('hellowwworld')
def datetime_now(request):
    now = datetime.datetime.now()
    html = 'My clock says that it is now %s' % now
    return HttpResponse(html)
def whoru(request):
    uname = request.GET['urname']
    uland = request.GET['uland']
    response = 'You are ' + uname + ' and you come from ' + uland
    return HttpResponse(response)
# Create your views here.


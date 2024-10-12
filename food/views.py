from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("<h1>Im index</h1>")
    return render(request, 'food/index.html')




def show(request):
    return HttpResponse("<h1>im Show me</h1>")
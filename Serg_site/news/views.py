from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request)
    return HttpResponse('Hlow World')


def test(request):
    print(request)
    return HttpResponse('<h1>Сторінка ТЕСТ</h1>')

def test2(request):
    print(request)
    return HttpResponse('<h1>222222222222222</h1>')
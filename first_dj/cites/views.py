from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h3>главная</h3><h1 style="color:red"><h>информация стран</h1> \
                            <li><a href= "http://127.0.0.1:8000/history">история</a></li>\
                            <li><a href= "http://127.0.0.1:8000/cities">города</a></li>\
                            <li><a href= "http://127.0.0.1:8000/facts">факты</a></li>')

def history(request):
    return HttpResponse('<h3>история страны</h3>')

def cities(request):
    return HttpResponse('<h3>города</h3> <ul><li><a href= "http://127.0.0.1:8000/cities/moscow">москва<a></il><li><a href= "http://127.0.0.1:8000/cities/piter">питер <a></il></ul>')

def cities_moscow(request):
    return HttpResponse('<h3>москва</h3> <ul><li>ок</il></ul>')

def cities_piter(request):
    return HttpResponse('<h3>питер</h3> <ul><li>лол </il></ul>')

def facts(request):
    return HttpResponse('<h3>факты о стране </h3>')



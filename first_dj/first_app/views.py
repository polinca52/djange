from django.shortcuts import render, HttpResponse

def index(request):
    user_agent = request.headers.get('User-Agent')
    return HttpResponse('<h3>главная</h3><h1 style="color:red">компания ЛАБУБУ</h1> <li><a href= "http://127.0.0.1:8000/news">новости</a></li>\
                            <li><a href= "http://127.0.0.1:8000/managment">менеджмент</a></li>\
                            <li><a href= "http://127.0.0.1:8000/about">о нас</a></li>\
                            <li><a href= "http://127.0.0.1:8000/contacts">контакты</a></li>\
                            <li><a href= "http://127.0.0.1:8000/branches">филиалы</a></li></ul>')

def news(request):
    return HttpResponse('<h3>новости</h3> <ul><li>новости</il><li>новости</il><li>новости</il></ul>')

def first_news(request):
    return HttpResponse('<h3>новости</h3> <ul><li>макан и баста зотят выпустить трек, но тк у макана нет телефона они не могут договорится о времяни, сейчас они дома </il></ul>')

def managment(request):
    return HttpResponse('<h3>руководство</h3>\
                         <h2>macan</h2> <p>СЕО компании</p> \
                        <h2>баст</h2> <p>top-manager</p>\
                        <a href = "http://127.0.0.1:8000"> назад</a>')

def about(request):
    return HttpResponse('<h3>о компании</h3> <p> выпуск песни макан и басты</p>')

def contacts(request):
    return HttpResponse('<h3>контакты</h3> <ul><li>номер макана: у него нет телефона</il><li>номер басты: ток голубиной почтой </il></ul>')

def branches(request):
    return HttpResponse('<h3>филиал</h3> <ul><li><a href= "http://127.0.0.1:8000/branches/moscow">москва<a></il><li><a href= "http://127.0.0.1:8000/branches/piter">питер <a></il></ul>')

def branches_moscow(request):
    return HttpResponse('<h3>москва</h3> <ul><li>макан</il></ul>')

def branches_piter(request):
    return HttpResponse('<h3>питер</h3> <ul><li>баста </il></ul>')


## Create your views here.*
##4 5
#from datetime import datetime
#week_list = ['monday', 'tuesday', 'wenesday', 'thursday', 'friday', 'saturday', 'sunday']
#
#from random import choice
#punch_lits = ['«Хорошо там, где меня нет… Но ничего, я и туда доберусь!',
#'«Злопамятность — признак старости».',
#'«Английский — простой, но очень трудный язык. Он состоит из одних иностранных слов, которые к тому же неправильно произносятся».',
#'«Детство заканчивается тогда, когда на тебя уже странно смотрят в песочнице!».',
#'Я на виски-диете. Я уже потерял три дня.']
#
#
#def today(request):
#    return HttpResponse(f'сегодня:{week_list[datetime.now().weekday()]}')
#
#def punch(request):
#    return HttpResponse(f'мудрая цитата:{choice(punch_lits)}')
#
#
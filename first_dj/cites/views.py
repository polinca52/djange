#from django.shortcuts import render, HttpResponse
#
## Create your views here.
#
#def index(request):
#    return HttpResponse('<h3>главная</h3><h1 style="color:red"><h>информация стран</h1> \
#                            <li><a href= "http://127.0.0.1:8000/history">история</a></li>\
#                            <li><a href= "http://127.0.0.1:8000/cities">города</a></li>\
#                            <li><a href= "http://127.0.0.1:8000/facts">факты</a></li>')
#
#def history(request):
#    return HttpResponse('<h3>история страны</h3>')
#
#def cities(request):
#    return HttpResponse('<h3>города</h3> <ul><li><a href= "http://127.0.0.1:8000/cities/moscow">москва<a></il><li><a href= "http://127.0.0.1:8000/cities/piter">питер <a></il></ul>')
#
#def cities_moscow(request):
#    return HttpResponse('<h3>москва</h3> <ul><li>ок</il></ul>')
#
#def cities_piter(request):
#    return HttpResponse('<h3>питер</h3> <ul><li>лол </il></ul>')
#
#def facts(request):
#    return HttpResponse('<h3>факты о стране </h3>')



#Tacs
from django.shortcuts import render, HttpResponse

# Create your views here.

#def index(request):
#    return render(request,'index.html')

from .forms import FormOrder
from datetime import datetime  
from datetime import datetime
from .models import Order


def index(request):
      orders = Order.objects.all()
      return render(request, 'index.html', context={'orders':orders})

def form_order(request):
      if request.method == 'POST':
            name = request.POST.get('name')
            last_name = request.POST.get('f_name')
            email = request.POST.get('email')
            product = request.POST.get('product')
            order = Order.objects.create(name=name, f_name = last_name, email = email, product = product)
            order.save()
            return render(request, 'index.html',)
      else:
            form = FormOrder()
            return render(request, 'form.html', context={'form':form})




#def football(request):
#    return render(request,'football.html')

#list_pro= [['томаты','мясо','перец','лук'],['картофель','тесто','сметана']]

#def recipe(request):
#      dish = request.GET.get('recipe')
#      if dish == 'gouiash':
#            list_ingr = list_pro[0]
#      else:
#            list_ingr= list_pro[1]
#      return render(request, 'recipe.html', context={'title':dish, 'list_ingr':list_ingr})







#def hoskey(request):
#    return HttpResponse('<h3>хокей </h3>')
#
#def basketball(request):
#    return HttpResponse('<h3>баскетбол </h3>')
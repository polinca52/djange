"""
URL configuration for first_dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
#from first_app.views import branches_piter, branches_moscow, index,news,branches, first_news, managment, about, contacts
#from cites.views import history, cities, facts, index, cities_piter, cities_moscow
#from cites.views import football, index, recipe
from first_app.views import user_form, index, user


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', recipe),  
    
    #path('news/first_news', first_news),
    #re_path(r'^news/', news),
    #path('managment', managment),
    #path('about', about),
    #path('contacts', contacts),
    #path('branches/piter', branches_piter),
    #path('branches/moscow', branches_moscow),
    #re_path(r'^branches/', branches),
    #path('today/', today),
    #path('punch/', punch)
    ##path('history', history),
    ##path('cities', cities),
    ##path('facts', facts),
    ##path('cities/piter', cities_piter),
    ##path('cities/moscow', cities_moscow)
    #path('basketball', basketball),
    #path('hoskey', hoskey),
    #path('/football',football, name='football'),
    path('', index),
    path('user/', user, name='registration')
   
]

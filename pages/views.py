from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# all the views here

def home(request):

    context = {'pagename': 'Hello man', 'name':'imran',}
    template = "pages/home.html"

    return render(request, template, context)


    


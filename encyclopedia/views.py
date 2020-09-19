from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

import re
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_content(request, title):
    get_entry = util.get_entry(title)
    if get_entry == None:
        return render(request, "encyclopedia/error.html", {
            "title": title.upper(),
        })           
    else:
        return render(request,"encyclopedia/entries.html", {
            "title": title.upper(),
            "content": util.get_entry(title)
        })

def search(request):
    #check request method to be GET
    if request.method == "GET":
        #pull the data from the form with name ="q"
        query = request.GET.get("q")
        #pass in user's data(query) to util.get_entry
        if util.get_entry(query):
            #redirect to get_content view replacing arg from get_content with user's input data
            return HttpResponseRedirect(reverse("encyclopedia:get_content", kwargs={"title": query}))
        
          
            

            

        
          
        
    
                






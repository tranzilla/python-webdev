from django.shortcuts import render

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


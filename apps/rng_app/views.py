from django.shortcuts import render, redirect as redir
from django.utils.crypto import get_random_string



def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
    if "random" not in request.session:
        return redir("/random")
    else:
        if request.method == "GET":
            return render(request, "index.html")
        if request.method == "POST":
            return redir("/random")
    

def random(request):
    if request.method == "GET":
        request.session["random"] = get_random_string(length=14)
    
        request.session["count"] += 1
        return redir("/")

def reset(request):
    if request.method =="GET":
        request.session["count"] = 0
        return redir("/")
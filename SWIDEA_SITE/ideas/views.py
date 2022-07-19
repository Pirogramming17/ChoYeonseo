from re import template
from django.shortcuts import render, redirect, get_object_or_404
from .models import Devtool, Idea

def idea_home(request):
    ideas = Idea.objects.all()
    context = {
        "ideas" : ideas,
    }
    return render(request, template_name="ideas/idea_home.html", context=context)

def idea_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        selected_devtool = request.POST["devtool"]
        
        Idea.objects.create(title=title, image=image, content=content, interest=interest, devtool=selected_devtool)
        
        return redirect("/")
    
    ideas = Idea.objects.all()
    context = {
        "ideas":ideas
    }
    return render(request, template_name="ideas/idea_create.html", context=context)
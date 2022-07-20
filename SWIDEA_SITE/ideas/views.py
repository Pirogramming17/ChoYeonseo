from django.shortcuts import render, redirect
from .models import Devtool, Idea

#idea page view
def idea_home(request):
    sort= request.GET.get('sort', "")
    if sort == 'title':
        ideas = Idea.objects.all().order_by('-title')
    else:
        ideas = Idea.objects.all()
    context = {
        "ideas" : ideas,
    }
    return render(request, template_name="ideas/idea_home.html", context=context)

def idea_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES.get("image",False)
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = Devtool.objects.get(name = request.POST["devtool"])
        
        Idea.objects.create(title=title, image=image, content=content, interest=interest, devtool=devtool)
        
        return redirect("/")
    
    devtools=Devtool.objects.all()
    context = {
        "devtools":devtools,
    }
    return render(request, template_name="ideas/idea_create.html", context=context)

def idea_detail(request, id):
    idea = Idea.objects.get(id=id)
    context={
        "idea":idea,
    }
    return render(request, template_name="ideas/idea_detail.html", context=context)

def idea_update(request,id):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES.get("image", False)
        content = request.POST["content"]
        interest = request.POST["interest"]
        selected_devtool = Devtool.objects.get(name = request.POST["devtool"])
        devtool = selected_devtool
        
        Idea.objects.filter(id=id).update(title=title, image=image, content=content, interest=interest, devtool=devtool)
        
        return redirect(f"/idea/detail/{id}")
    
    elif request.method == "GET":
        idea = Idea.objects.get(id=id)
        devtools = Devtool.objects.all()
        context ={
            "idea":idea,
            "devtools":devtools,
        }
        return render(request, template_name="ideas/idea_update.html", context=context)

def idea_delete(request, id):
    if request.method == "POST":
        Idea.objects.filter(id=id).delete()
        return redirect('/')
    
    
#개발툴 페이지 view   
def devtool_list(request):
    devtools = Devtool.objects.all()
    context={
        "devtools": devtools,
    }
    return render(request, template_name="devtools/devtool_list.html", context=context)

def devtool_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        type = request.POST["type"]
        explain = request.POST["explain"]
        
        Devtool.objects.create(name=name, type=type, explain=explain)
        
        return redirect("/devtool")
    
    devtools = Devtool.objects.all()
    context={
        "devtools":devtools
    }
    return render(request, template_name="devtools/devtool_create.html", context=context)

def devtool_detail(request,id):
    devtool=Devtool.objects.get(id=id)
    context={
        "devtool":devtool,
    }
    return render(request, template_name="devtools/devtool_detail.html", context=context)

def devtool_update(request,id):
    if request.method == "POST":
        name = request.POST["name"]
        type = request.POST["type"]
        explain = request.POST["explain"]
        
        Devtool.objects.filter(id=id).update(name=name, type=type, explain=explain)
        
        return redirect(f"/devtool/detail/{id}")
    elif request.method == "GET":
        devtool = Devtool.objects.get(id=id)
        context={
            "devtool":devtool
        }
        return render(request, template_name="devtools/devtool_update.html", context=context)

def devtool_delete(request,id):
    if request.method == "POST":
        Devtool.objects.filter(id=id).delete()
        return redirect("/devtool")
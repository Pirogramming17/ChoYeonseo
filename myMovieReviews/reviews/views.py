from platform import release
from django.shortcuts import redirect, render

import reviews

from .models import Review

def home(request):
    reviews = Review.objects.all()
    context = {
        "reviews":reviews
    }
    return render(request, template_name="reviews/home.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        r_year = request.POST["r_year"]
        genre = request.POST["genre"]
        grade = request.POST["grade"]
        r_time = request.POST["r_time"]
        r_content = request.POST["r_content"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        
        Review.objects.create(title=title, r_year=r_year, genre=genre, grade=grade, r_time=r_time, r_content=r_content, director=director, actor=actor)
        
        return redirect("/")
    
    return render(request, template_name="reviews/create.html", context={})

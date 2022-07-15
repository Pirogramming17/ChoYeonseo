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
    
    context = {
        "genres": Review.GENRE_CHOICES
    }
    
    return render(request, template_name="reviews/create.html", context=context)

def detail(request, id):
    review = Review.objects.get(id=id)
    hour = review.r_time // 60
    minute = review.r_time % 60
    context = {
        "review" : review,
        "hour": hour,
        "minute": minute
    }
    return render(request, template_name="reviews/detail.html", context=context)

def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        r_year = request.POST["r_year"]
        genre = request.POST["genre"]
        grade = request.POST["grade"]
        r_time = request.POST["r_time"]
        r_content = request.POST["r_content"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        
        review = Review.objects.filter(id=id).update(title=title, r_year=r_year, genre=genre, grade=grade, r_time=r_time, r_content=r_content, director=director, actor=actor)
        
        return redirect(f"/review/{id}")
    
    elif request.method =="GET":
        review = Review.objects.get(id=id)
        context = {
            "review":review,
            "genres":Review.GENRE_CHOICES
        }
        return render(request, template_name="reviews/update.html", context=context)

def delete(request, id):
    review=Review.objects.filter(id=id)
    review.delete()
    return redirect("/")
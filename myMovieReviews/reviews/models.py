from platform import release
from tabnanny import verbose
from time import time
from django.db import models

class Review(models.Model):
    GENRE_CHOICES = (
        ('AT','Action'),
        ('SF','SF'),
        ('RM','Romance'),
        ('CM', 'Comedy'),
        ('AM', 'Animation'),
        ('TR', 'Thriller')
        
    )
    
    title = models.CharField(max_length= 50, verbose_name="제목")
    r_year = models.IntegerField(verbose_name="개봉년도")
    genre= models.CharField(max_length=2, choices=GENRE_CHOICES, verbose_name="장르")
    grade =models.FloatField(verbose_name="별점")
    r_time = models.IntegerField(verbose_name="러닝타임")
    r_content = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=30,verbose_name="감독")
    actor = models.CharField(max_length=30, verbose_name="배우")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
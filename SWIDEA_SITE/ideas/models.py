from django.db import models

class Devtool(models.Model):
    name = models.CharField(max_length=50, verbose_name="이름")
    type = models.CharField(max_length=50, verbose_name="종류")
    explain = models.TextField(verbose_name="설명")

class Idea(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목") 
    image = models.ImageField(blank=True, upload_to="ideas/%Y%m%d", verbose_name="이미지")
    content = models.TextField(verbose_name="컨텐츠")
    interest = models.IntegerField(verbose_name="관심도")
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, related_name="idea_devtool" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
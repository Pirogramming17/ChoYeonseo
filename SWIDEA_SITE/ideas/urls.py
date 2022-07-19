from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ideas"
urlpatterns = [
    path('', views.idea_home, name="idea_home"),
    path('create', views.idea_create, name="idea_create")
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
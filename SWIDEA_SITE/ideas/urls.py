from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ideas"
urlpatterns = [
    path('', views.idea_home, name="idea_home"),
    path('create', views.idea_create, name="idea_create"),
    path('idea/detail/<int:id>', views.idea_detail, name="idea_detail"),
    path('idea/update/<int:id>', views.idea_update, name="idea_update"),
    path('idea/delete/<int:id>', views.idea_delete, name="idea_delete"),
    path('devtool', views.devtool_list, name="devtool_list"),
    path('devtool/create', views.devtool_create, name="devtool_create"),
    path('devtool/detail/<int:id>', views.devtool_detail, name="devtool_detail"),
    path('devtool/update/<int:id>', views.devtool_update, name="devtool_update"),
    path('devtool/delete/<int:id>', views.devtool_delete, name="devtool_delete")
    ]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
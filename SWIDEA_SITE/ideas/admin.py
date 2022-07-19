from django.contrib import admin
from .models import Idea, Devtool

@admin.register(Devtool)
class DevtoolAdmin(admin.ModelAdmin):
    pass

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    pass



from django.contrib import admin
from .models import memeData

# Register your models here.

@admin.register(memeData)
class memeDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    #pass
    
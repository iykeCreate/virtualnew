from django.contrib import admin
from.models import Post


# Register your models here.
class PostDB(admin.ModelAdmin):
    list_display=[
         "Title","Text"," Author","Create_date","Publisher_date"
    ]

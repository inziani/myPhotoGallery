from django.contrib import admin
from gallery.models import Post

# Register your models here.

admin.site.register(Post, admin.ModelAdmin)

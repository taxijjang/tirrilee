from django.contrib import admin
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'classification','writer')

admin.site.register(Posts, PostsAdmin)


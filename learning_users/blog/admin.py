from django.contrib import admin
from blog.models import Post,Comment

# Register your models here.

# Change the way posts are displayed on the admin page
class PostAdmin(admin.ModelAdmin):

    fields = ['author', 'title', 'create_date', 'published_date','text']

    # enable searching through posts on the admin page
    search_fields = ['title', 'text', 'published_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

from django.contrib import admin
from blog.models import Post,Comment

# Register your models here.

# Change the way posts are displayed on the admin page
class PostAdmin(admin.ModelAdmin):

    fields = ['author', 'title', 'create_date', 'published_date','text']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

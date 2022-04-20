from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {
        'slug': ('title', )
    }
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'active', 'created')
    list_filter = ('active', 'created', 'updated',)
    search_fields = ('name', 'email', 'body')

# Register your models here.

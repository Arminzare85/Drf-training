from django.contrib import admin
from .models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', )
    list_filter = ('status',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_time'
    ordering = ('-created_time',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
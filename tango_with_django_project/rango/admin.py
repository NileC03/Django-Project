from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    
admin.site.register(Category, CategoryAdmin)
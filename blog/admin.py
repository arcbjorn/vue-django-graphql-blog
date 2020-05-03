from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    fields = ('category_name',)

class LanguageAdmin(admin.ModelAdmin):
    fields = ('language_name',)

class PostAdmin(admin.ModelAdmin):
    fields = ('post_name', 'post_category', 'post_language',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Post, PostAdmin)
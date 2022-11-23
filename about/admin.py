from django.contrib import admin
from .models import Category, LatestPosts, About


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    search_fields = ('category',)


class LatestPostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title',)
    prepopulated_fields = ({'slug': ('title',)})


admin.site.register(Category, CategoryAdmin)
admin.site.register(LatestPosts, LatestPostsAdmin)
admin.site.register(About)

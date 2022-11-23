from django.contrib import admin
from .models import Post, Comment, Tag, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    search_fields = ('category',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class CommentInLineAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLineAdmin]
    list_display = ('id', 'title', 'category', 'created_at')
    list_filter = ('created_at', 'updated_at', 'category', 'tag')
    search_fields = ('title',)
    readonly_fields = ('updated_at', 'created_at')
    prepopulated_fields = ({'slug': ('title',)})
    filter_horizontal = ('tag',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'name', 'email', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = list_filter
    search_fields = ('name', 'email')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)


from django.contrib import admin
from .models import Article, Paragraph, Comment

class ParagraphInline(admin.StackedInline):
    model = Paragraph
    extra = 0

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ParagraphInline,
        CommentInline
    ]

admin.site.register(Article, ArticleAdmin)
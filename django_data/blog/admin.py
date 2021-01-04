from django.contrib import admin
from .models import Article, Paragraph, Comment, RichText

class ParagraphInline(admin.StackedInline):
    model = Paragraph
    extra = 0

class RichTextInline(admin.StackedInline):
    model = RichText
    extra = 0

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ParagraphInline,
        RichTextInline,
        CommentInline
    ]

admin.site.register(Article, ArticleAdmin)
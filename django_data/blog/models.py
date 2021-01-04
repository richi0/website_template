from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.URLField()
    preface = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    def get_text(self):
        paragraps = self.paragraphs.all()
        rich_text = self.richtexts.all()
        text = list(paragraps) + list(rich_text)
        return sorted(text, key=lambda obj: obj.order)

    class Meta:
        ordering = ['-created_at']


class Paragraph(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    article = models.ForeignKey(
        Article, related_name="paragraphs", on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class RichText(models.Model):
    content = RichTextField()
    article = models.ForeignKey(
        Article, related_name="richtexts", on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return "RichText Element"

    class Meta:
        ordering = ['order']


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']

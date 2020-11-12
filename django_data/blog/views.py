from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.urls import reverse
from .models import Article, Comment
from .forms import CommentForm


class BlogHomePageView(ListView):
    queryset = Article.objects.all()
    template_name = 'blog/home.html'

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

def create_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            article = Article.objects.get(pk=pk)
            obj = form.save(commit=False)
            obj.article = article
            obj.save()
            return redirect(reverse('article_detail', args=[str(pk)]))
        else:
            return redirect(reverse('article_detail', args=[str(pk)]))
    else:
        return redirect(reverse('article_detail', args=[str(pk)]))
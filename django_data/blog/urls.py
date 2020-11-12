from django.urls import path
from .views import BlogHomePageView, DetailArticleView, create_comment

urlpatterns = [
    path('', BlogHomePageView.as_view(), name='blog_index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='article_detail'),
    path('create_comment/<int:pk>/', create_comment, name='create_comment')
]

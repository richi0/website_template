from django.test import TestCase
from django.urls import reverse, resolve

from .views import BlogHomePageView, DetailArticleView, create_comment
from .models import Article, Paragraph, Comment

class BlogHomePageViewTests(TestCase):

    def setUp(self):
        url = reverse("blog_index")
        self.response = self.client.get(url)

    def test_blog_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_blog_homepage_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/home.html")

    def test_blog_homepage_contains_correct_html(self):
        self.assertContains(self.response, "wymco")

    def test_blog_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, "No content")

    def test_blog_homepag_view_class(self):
        view = resolve(reverse("blog_index"))
        self.assertEqual(view.func.__name__,
                         BlogHomePageView.as_view().__name__)

class DetailArticleViewTests(TestCase):

    def setUp(self):
        self.blog_post = get_blog_post()
        self.url = self.blog_post.get_absolute_url()
        self.response = self.client.get(self.url)

    def test_blog_detail_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_blog_detail_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "blog/detail.html")

    def test_blog_detail_contains_correct_html(self):
        self.assertContains(self.response, "wymco")
        self.assertContains(self.response, "Richie")
        self.assertContains(self.response, "Title of article")
        self.assertContains(self.response, "https://example.com/image1.png")
        self.assertContains(self.response, "Just some text")
        self.assertContains(self.response, "Paragraph1")
        self.assertContains(self.response, "This is the conten for the first paragraph")
        self.assertContains(self.response, "Paragraph2")
        self.assertContains(self.response, "This is the conten for the second paragraph")
        self.assertContains(self.response, "Joe")
        self.assertContains(self.response, "This is the first comment")
        self.assertNotContains(self.response, "Ylmaz")
        self.assertNotContains(self.response, "This is the second comment")

    def test_blog_detail_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, "No content")

    def test_blog_detail_view_class(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__,
                         DetailArticleView.as_view().__name__)

def get_blog_post():
    article = Article.objects.create(
        author="Richie",
        title="Title of article",
        image="https://example.com/image1.png",
        preface="Just some text",
    )
    
    paragraph1 = Paragraph.objects.create(
        title="Paragraph1",
        content="This is the conten for the first paragraph",
        article=article,
        order=1
    )

    paragraph2 = Paragraph.objects.create(
        title="Paragraph2",
        content="This is the conten for the second paragraph",
        article=article,
        order=2
    )

    comment1 = Comment.objects.create(
        name="Joe",
        email="email@example.com",
        content="This is the first comment",
        article=article,
        approved=True
    )

    #Not approved and will not show on the page
    comment2 = Comment.objects.create(
        name="Ylmaz",
        email="email2@example.com",
        content="This is the second comment",
        article=article
    )
    return article
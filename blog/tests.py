from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.post = Post.objects.create(
            title="pickle",
            body="refreshing",
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title="Snicker")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "pickle")
        self.assertEqual(f"{self.post.author}", "tester")
        self.assertEqual(f"{self.post.body}", "refreshing")

    def test_post_list_view(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "blog-list.html")

    def test_post_detail_view(self):
        response = self.client.get(reverse("blog_detail", args="1"))  #'/Posts/1/')
        no_response = self.client.get("/Posts/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "refreshing")
        self.assertTemplateUsed(response, "blog-detail.html")

    def test_post_create_view(self):
        response = self.client.post(
            reverse("blog_create"),
            {
                "title": "Chicharrones",
                "body": "Low carb",
                "author": self.user,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chicharrones")
        self.assertContains(response, "Low carb")
        self.assertTemplateUsed(response, "blog-create.html")

    def test_post_update_view(self):
        response = self.client.post(
            reverse("blog_update", args="1"),
            {
                "title": "Updated title",
                "body": "Updated body",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_post_update_view_redirect(self):
        response = self.client.post(
            reverse("blog_update", args="1"),
            {
                "title": "Updated title",
                "body": "Updated body",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Updated title")

        self.assertTemplateUsed("blog-detail.html")

    def test_post_delete_view(self):
        response = self.client.get(reverse("blog_delete", args="1"))
        self.assertEqual(response.status_code, 200)
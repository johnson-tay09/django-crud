from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    template_name = "blog-list.html"
    model = Post


class BlogDetailView(DetailView):
    template_name = "blog-detail.html"
    model = Post


class BlogCreateView(CreateView):
    template_name = "blog-create.html"
    model = Post
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    template_name = "blog-update.html"
    model = Post
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    template_name = "blog-delete.html"
    model = Post
    success_url = reverse_lazy("list")

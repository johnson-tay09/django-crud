from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="list"),
    path("detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("new/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/edit", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete", BlogDeleteView.as_view(), name="blog_delete"),
]

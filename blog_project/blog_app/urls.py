from django.urls import path

from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<slug:post_slug>', views.post_detail, name="post_detail"),
    path("results/", views.search_post, name="search")
]
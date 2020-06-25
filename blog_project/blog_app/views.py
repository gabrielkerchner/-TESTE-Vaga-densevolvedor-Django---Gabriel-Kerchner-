from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category


# Create your views here.

def blog(request):

    list_posts = Post.objects.order_by('-publicacao')
    paginator = Paginator(list_posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog_app/blog.html", {'list_post':list_posts, 'page_obj': page_obj, "search_post": search_post})

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, "blog_app/post_detail.html", {"post":post })

def search_post(request):
  query = request.GET.get('q')
  posts = Post.objects.filter(
      Q(title__icontains=query) |
      Q(content__icontains=query) |
      Q(categories__name__icontains=query)
      )
  return render(request, 'blog_app/search.html', {'posts': posts})


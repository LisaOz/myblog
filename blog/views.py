from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.


def post_detail(request, year, month, day, post):  # post_detail view for retrieve post with a given date
    post = get_object_or_404(
        Post,
       
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
 )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )


def post_list(request):  # our first view with 1 parameter 'request' object
    posts = Post.published.all()  # retrieve all posts with 'published' status
    return render(  # return the list of posts with the given template
        request,  # request object
        'blog/post/list.html',  # template path
    {'posts': posts}  # context variables to render template
    )

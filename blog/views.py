from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.


def post_detail(request, id):  # post_detail view
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
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

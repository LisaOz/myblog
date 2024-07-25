from .forms import EmailPostForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404, render

# Create your views here.

class PostListView(ListView):
    """
    Class-based view to list published posts with pagination
    """
    queryset = Post.published.all() # use custom QuorySet instead of retrieving all objects
    context_object_name = 'posts'# query results
    paginate_by = 3 # pagination result returns 3 objects per page
    template_name = 'blog/post/list.html' #custom template to render the page with template_name

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


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(  # retrieve the published post by id
        Post,
        id=post_id
        status=Post.Status.PUBLISHED
    )
    if request.method == 'POST':   # Form is being submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form passed with validation
            cd = form.cleaned_data
        else:
            form = EmailPostForm()
        return render(
            request,
            'blog/post/share.html',
            {
                'post': post,
                'form': form
            }
        )

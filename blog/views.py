from django.core.mail import send_mail
from .forms import EmailPostForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    """
    View to share a post via email
    """
    
    post = get_object_or_404(  # retrieve the published post by id
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False


    if request.method == 'POST':
        form = EmailPostForm(request.POST) # Form was submitted
        if form.is_valid():
            cd = form.cleaned_data # Form validation passed 
            post_url = request.build_absolute_uri(post.get_absolute_url())
            
            subject = (
                f"{cd['name']} ({cd['email']}) "
                f"recommends you {post.title}"
            )

            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}\'s comments: {cd['comments']}"
            )

            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        'blog/post/share.html',
        {
            'post': post,
            'form': form,
            'sent': sent
        }
    )
            
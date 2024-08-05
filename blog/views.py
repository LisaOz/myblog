from django.db.models import Count
from django.core.mail import send_mail
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import TrigramSimilarity
from taggit.models import Tag
from .models import Post
from .forms import EmailPostForm, CommentForm, SearchForm



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

    # Add the list of comments and the comment form
    comments = post.comments.filter(active=True) # retrieve the list of active comments
    form = CommentForm() # create the instance of the Comment Form, display the form

    # Implement finding posts with the similar tags
    post_tags_ids = post.tags.values_list('id', flat=True) # return tag ids values and turn them from tuple values to simple
    similar_posts = Post.published.filter(
        tags__in=post_tags_ids # chose the post with the same tags
    ).exclude(id=post.id) # exlude the current post from the recommended list of posts
    similar_posts = similar_posts.annotate(  # order the posts with similar tags
        same_tags=Count('tags')  # 
    ).order_by('-same_tags', '-publish')[:3] # recommend 3 posts with the same tags, starting with max tags number
    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form,
            'similar_posts': similar_posts 
        }
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
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    comment = None
    form = CommentForm(data=request.POST) # the comment posted
    if form.is_valid():
        comment = form.save(commit=False) # Create a comment object  without saving it into the database
        comment.post = post # Assign the post to the comment
        comment.save() # Save the comment to the database
    return render(
        request,
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment
        }
    )

def post_list(request, tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 3) # display 3 posts on the page
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'tag': tag,

        }
    )

"""
Create search view
"""
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:  # use the GET parameter to receive  URL with the query parameter
        form = SearchForm(request.GET) 
        if form.is_valid():
            query = form.cleaned_data['query']
            results = (
                Post.published.annotate( # Search posts with the TrigramSimilarity
                    similarity=TrigramSimilarity('title', query),
                )
                .filter(similarity__gt=0.1)
                .order_by('-similarity')
            )
    return render(
        request,
        'blog/post/search.html',
        {
            'form': form,
            'query': query,
            'results': results
        }
    )
    
def homepage(request):
    posts = Post.published.all()
    return render(request, 'blog/homepage.html', {'posts': posts})
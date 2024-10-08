from django.db.models import Count
from django import template
from ..models import Post
import markdown
from django.utils.safestring import mark_safe

register = template.Library()
@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=10):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(  # aggregate the total number of comments for each post
        total_comments=Count('comments') # save the number of comments for each Post
    ).order_by('-total_comments')[:count] # order posts with comments in the desc order and limit by 5

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text, extensions=['extra']))
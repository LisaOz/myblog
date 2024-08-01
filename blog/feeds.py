import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):

    title = 'My blog'  # corresponds to the <title> RSS element
    link = reverse_lazy('blog:post_list') # generate URL for the <link> attr RSS
    description = 'New posts in my blog' # <description> RSS

    def items(self):
        return Post.published.all()[:5]  # return items to be included in the feed
    
    def item_title(self, item): # returns title of the post
        return item.title
    
    def item_description(self, item): # returns description of the post
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item): # returns the publication date of the post
        return item.publish

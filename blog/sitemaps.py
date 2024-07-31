"""
Define a custom sitemap by inheriting the Sitemap class of the sitemaps module.
changefreq and priority attr indicate the change frequency of the post pages 
and their relevance in the website

"""

from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly" # indicates how frequently the content of the post pages is expected to change
    priority = 0.9 # returns the list of items to be included in the sitemap (all published posts).

    def items(self):
        return Post.published.all() # queries the Post model to get all posts that have been published. 
    
    def lastmod(self, obj): # method to return the last modification date of each item in the sitemap
        return obj.updated # returns the updated attribute of the Post object with date and time when the post was last updated
        
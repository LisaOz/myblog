from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit. managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    tags = TaggableManager() 
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'# create slug with unique name and published date
    
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # store the last date and time when post was published
    created = models.DateTimeField(auto_now_add=True) # store the last date and time when post was created
    updated = models.DateTimeField(auto_now=True)  # store the last date and time when post was updated
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )


    objects = models.Manager() # Default manager
    published = PublishedManager() # Custom manager

    class Meta:
        ordering = ['-publish']  # sort results by the 'publish' field in reverse chronological order
        indexes = [models.Index(fields=['-publish'])]  # added index for the 'publish' field, in descending order

    def __str__(self):
        return self.title

    # Function to build the URL dynamically using the URL name defined in the URL patterns
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
                ]
        )


"""
Comment Model
"""
class Comment(models.Model):
    post = models.ForeignKey( # foreign key associates each comment with a single post; many-to-one relationship
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) # control the status, will enabling deactivating the inappropriate comments

    class Meta:
        ordering = ['created']  # to sort the comments in chronological order
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
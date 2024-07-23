from django.conf import settings
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
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

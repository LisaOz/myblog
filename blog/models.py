from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.Charfield(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # store the last date and time when post was published
    created = models.DateTimeField(auto_now_add=True) # store the last date and time when post was created
    updated = models.DateTimeField(auto_now=True)  # store the last date and time when post was updated

    class Meta:
        ordering = ['-publish'] # sort results by the 'publish' field in reverse chronological order
        indexes = [models.Index(fields=['-publish'])]  # added index for the 'publish' field, in descending order
    def __str__(self):
        return self.title

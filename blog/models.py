from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Custom model manager that performs special queries that fit my needs
# This manager returns all post filtered by the status "published
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# Post Model
class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # define default model manager
    published = PublishedManager()  # define custom model manager


    # Metadata Class
    # Sorts results by the "publish" field in descending order "-"
    class Meta:
        ordering = ('-publish',)

    # Getter method that returns the title of the blog
    def __str__(self):
        return self.title

    
    # Define Canonical URL for a blog resource (a blog)
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                    args=[self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug])


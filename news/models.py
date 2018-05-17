from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class News(models.Model):
    NEWS_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=128)

    # Slug using in urls
    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True, blank=True)

    # Author is owner of the Article
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE, null=True, blank=True)

    # Contest is short info about article, using as an introduction
    contest = models.CharField(max_length=300)
    text = models.TextField()

    # Publish date
    publish = models.DateTimeField(default=timezone.now)

    # Time after article creating
    created = models.DateTimeField(auto_now_add=True)

    # Last updating time
    updated = models.DateTimeField(auto_now=True)

    # Article status which can be published or not
    status = models.CharField(max_length=10, choices=NEWS_STATUS, default='draft')

    # Using for getting the last news
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
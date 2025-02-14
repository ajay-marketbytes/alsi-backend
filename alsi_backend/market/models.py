from django.db import models

class BlogBanner(models.Model):
    title_highlights = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_banner/', null=True, blank=True)
    blog_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class BlogEntry(models.Model):
    blog_title = models.CharField(max_length=2000)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_entries/', null=True, blank=True)
    blog_slug = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_title = models.CharField(max_length=2000)
    date = models.CharField(max_length=500, null=True, blank=True)
    time = models.CharField(max_length=500, null=True, blank=True)
    intro = models.TextField(blank=True, null=True)
    additional_content = models.TextField()

    def __str__(self):
        return self.title

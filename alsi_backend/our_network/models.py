from django.db import models

class NetworkBanner(models.Model):
    title = models.CharField(max_length=255)
    title_highlight = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    highlights = models.TextField(null=True, blank=True)
    description = models.TextField()
    lists = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Network(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    position_top = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    position_left = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=500, null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
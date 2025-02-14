from django.db import models

class IndustryBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='industry_banner/')

    def __str__(self):
        return self.title
    
class IndustryEntry(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='industry_entries/')

    def __str__(self):
        return self.description if self.description else "No description"

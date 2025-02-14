from django.db import models

# Footer       
class Footer(models.Model):
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True) 
    email = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.location

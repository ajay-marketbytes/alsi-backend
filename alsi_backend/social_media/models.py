from django.db import models

class SocialMedia(models.Model):
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    thread = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"SocialMedia links (ID: {self.id})"
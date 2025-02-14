from django.db import models

class GalleryBanner(models.Model):
    image = models.ImageField(upload_to='gallery_banner/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    main_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    year = models.PositiveIntegerField()
    slug = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')

class GalleryVideo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='videos', on_delete=models.CASCADE)
    video_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"Video: {self.video_url}"

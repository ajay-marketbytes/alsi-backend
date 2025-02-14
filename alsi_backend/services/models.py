from django.db import models

class ServicesTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=255)
    service_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    subtitle = models.CharField(max_length=2000)
    link_url = models.CharField(max_length=255, null=True, blank=True)
    banner_image = models.ImageField(upload_to='services/')
    content_paragraphs = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    service = models.ForeignKey(Services, related_name='subcategories', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text_color = models.CharField(max_length=255)
    enable_fill_empty_cards = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

class Card(models.Model):
    subcategory = models.ForeignKey(Subcategory, related_name='cards', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cards/')

    def __str__(self):
        return self.title

class SpecializedServiceBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')

class SpecializedService(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='services/')
    dedicated_title = models.CharField(max_length=255)
    dedicated_image = models.ImageField(upload_to='services/')
    dedicated_paragraph = models.TextField(null=True, blank=True)
    link_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.description if self.description else "No description"

class SpecializedCategory(models.Model):
    service = models.ForeignKey(SpecializedService, related_name="subcategories", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text_color = models.CharField(max_length=7, default="#212529")  
    enable_fill_empty_cards = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class SpecializedCard(models.Model):
    category = models.ForeignKey(SpecializedCategory, related_name="cards", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="cards/", blank=True, null=True)

    def __str__(self):
        return self.title or "Empty Card"
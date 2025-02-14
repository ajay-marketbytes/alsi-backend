from django.db import models

# Banner
class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField() 
    link_name = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# ChooseUs
class ChooseUs(models.Model):  
    image = models.ImageField(upload_to='chooses/')
    title = models.CharField(max_length=255)
    description = models.TextField()  

    def __str__(self):
        return self.title

# Differentiators
class Differentiator(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()  

    def __str__(self):
        return self.title

class DifferentiatorEntry(models.Model):
    image = models.ImageField(upload_to='differentiators/')
    differentiator_title = models.CharField(max_length=255)  

    def __str__(self):
        return self.differentiator_title  

# Achievements
class Achievement(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class AchievementEntry(models.Model):
    image = models.ImageField(upload_to='achievements/')
    description = models.TextField()  

    def __str__(self):
        return self.description
    
# Highlights
class Highlight(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class HighlightEntry(models.Model):
    highlight_title = models.TextField()  

    def __str__(self):
        return self.highlight_title
    
# Industries 
class Industry(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class IndustryEntry(models.Model):
    entry_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='industry_entries/')
    title = models.CharField(max_length=255)
    description = models.TextField()  
    path_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


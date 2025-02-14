from django.db import models

class Banners(models.Model):
    title =  models.CharField(max_length=255)
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title
    
class OurStory(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='story/')
    description_first = models.TextField()  
    description_second = models.TextField() 
    description_third = models.TextField()   

    def __str__(self):
        return self.title

class OurTeam(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class OurTeamEntry(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mission(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class MissionEntry(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='mission/')
    description = models.TextField()  

    def __str__(self):
        return self.title

class Member(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class MemberEntry(models.Model):
    image = models.ImageField(upload_to='member_entries/')

    def __str__(self):
        return f"{self.member.title} - Entry" 
    
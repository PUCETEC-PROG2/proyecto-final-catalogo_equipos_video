from django.db import models

class DVD (models.Model):
    title = models.CharField(max_length=30, null=False)
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    genre = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=300, null=False)
    picture = models.ImageField(upload_to="pokemon_images")
    
    def __str__(self):
        return self.title

class VHS (models.Model):
    title = models.CharField(max_length=30, null=False)
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    genre = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=300, null=False)
    picture = models.ImageField(upload_to="pokemon_images")
    
    def __str__(self):
        return self.title
    
class VideoEquipments (models.Model):
    title = models.CharField(max_length=30, null=False)
    year = models.DateField(auto_now=False, auto_now_add=False, null=False)
    description = models.CharField(max_length=300, null=False)
    picture = models.ImageField(upload_to="pokemon_images")

    def __str__(self):
        return self.title
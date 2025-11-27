from django.db import models
class Author(models.Model):
    name = models.CharField (max_length=100)
    
    def __str__(self):
        return self.name

class Book (models.Model):
    title = models.CharField (max_length=200)
    Author = models.ForeignKey (Authour, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

class Libary (models.Model):
        name = models.CharField (max_length=100)
        location = models.CharField (max_length=200)
        books = models.ManyToManyField (Book)

class Libarian (models.Model):
    name = models.CharField (max_length=100)
    library = models.OneToOneField (Libary, on_delete=models.CASCADE)        


    

# Create your models here.

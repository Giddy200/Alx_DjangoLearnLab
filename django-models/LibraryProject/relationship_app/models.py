from django.db import models
class authour (models.Model):
    name = models.CharField (max_length=100)

class book (models.Model):
    title = models.CharField (max_length=200)
    author = models.ForeignKey (authour, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

class libary (models.Model):
        name = models.CharField (max_length=100)
        location = models.CharField (max_length=200)
        books = models.ManyToManyField (book)

class libarian (models.Model):
    name = models.CharField (max_length=100)
    library = models.OneToOneField (libary, on_delete=models.CASCADE)        


    

# Create your models here.

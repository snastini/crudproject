from django.db import models


# Create your models here.
class Booktype(models.Model):
    title = models.CharField(max_length=40)
    
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    datepublished = models.DateField(null= True, blank=True)
    numpages = models.IntegerField(null=True)
    booktype = models.ForeignKey(Booktype, on_delete=models.CASCADE, null=True)


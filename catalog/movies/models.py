from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100,verbose_name="Film adı")
    description = models.TextField(verbose_name="Film açıklaması")
    image = models.CharField(max_length=50,verbose_name="Film resmi")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Eklenme Tarihi")
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name

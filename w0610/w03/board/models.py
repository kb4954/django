from django.db import models

# Create your models here.
class board(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id},{self.name}"
    
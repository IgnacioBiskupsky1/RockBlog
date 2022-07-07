from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    body = models.TextField()
    time = models.DateTimeField()
   
    
    
    

    
def _str_ (self):
    return self.title



class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)


def _str_ (self):
    return self.name   
    

class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    


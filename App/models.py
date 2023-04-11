from django.db import models

class inicio (models.Model):
    titulo=models.CharField(max_length=60)
    contenido=models.CharField(max_length=60)
    imagen=models.ImageField(upload_to='inicio')

    def __str__(self):
        return self.titulo
    

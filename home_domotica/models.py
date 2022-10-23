from django.db import models

# Create your models here.
class PriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    titulo = models.TextField()
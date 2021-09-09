from django.db import models

class Jordan(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    release_date = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f'{self.name}'
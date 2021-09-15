from django.db import models

class Jordan(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    release_date = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    liked_by = models.ManyToManyField(
      'jwt_auth.User',
      related_name='liked_jordan',
      blank=True
    )

    def __str__(self):
        return f'{self.name}'

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
      related_name='liked_jordans',
      blank=True
    )

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    jordan = models.ForeignKey(
        Jordan,
        related_name='comments',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.jordan} - {self.id}'
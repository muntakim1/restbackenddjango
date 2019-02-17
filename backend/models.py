from django.db import models
from django.contrib.auth.models import User


class productModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile/',blank=True,null=True)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

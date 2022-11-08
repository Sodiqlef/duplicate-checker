from django.db import models

# Create your models here.


class Duplicates(models.Model):
    duplicate = models.TextField()

    def __str__(self):
        return str(self.id)

from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    # Добавьте дополнительные поля по необходимости

    def __str__(self):
        return self.title

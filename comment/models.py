from django.db import models

# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=64)
    imdb = models.CharField(max_length=16)
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date commented')

    def __str__(self):
        return self.text

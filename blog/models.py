from django.db import models

# Create your models here.


class post(models.Model):

    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500)
    # image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
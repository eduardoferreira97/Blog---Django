from django.db import models


class Post(models.Model):
    autho = models.CharField(max_length=150)
    text = models.TextField()
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text 

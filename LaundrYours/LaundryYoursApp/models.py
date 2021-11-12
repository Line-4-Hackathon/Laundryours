from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)
    body = models.TextField(verbose_name='내용',default="")

    def __str__(self):
        return self.title
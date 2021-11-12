from django.db import models

# Create your models here.
class Fiber(models.Model):
    name = models.CharField(max_length=15, default='') #소재
    image = models.ImageField(upload_to='images/', default='')
    cleaning = models.TextField(max_length=200, default='') #세탁 방법
    saves = models.TextField(max_length=200, default='', blank=True) #보관 방법
    # feature = models.TextField(max_length=200, default='', blank=True) #특징
    # caution = models.TextField(max_length=200, default='', blank=True) #주의 사항

    def __str__(self):
        return self.name
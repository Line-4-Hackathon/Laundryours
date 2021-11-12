from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    username = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(default = '')
    created_at = models.DateTimeField(auto_now_add = True) # 만든 날짜, 시각 자동 저장
    updated_at = models.DateTimeField(auto_now = True) # 수정 날짜, 시각 자동 저장
    like_user_set = models.ManyToManyField(User, related_name='like_user_set', through='Like')
    like_counting = models.IntegerField(default=0)
    view_counting = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]

    def like_count(self):
        return int(self.like_user_set.count())

class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post.title
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
# s使用entries 管理条目
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        return self.text[:50]
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    ''' 用户学习的主题 '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        ''' 返回模型的字符串表示 '''
        return self.text

class Entry(models.Model):
    ''' 学到的有关某个主题的具体知识 '''
    ''' 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错：
TypeError: __init__() missing 1 required positional argument: 'on_delete' '''
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        ''' 返回模型的字符串表示 '''
        return self.text[:50] + "..."
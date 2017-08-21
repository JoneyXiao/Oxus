from django.db import models

# Create your models here.

ROLE_CHOICE = (
    (1, u'管理员'),
    (2, u'普通用户')

)

class UserInfo(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=16, default=11111111111)
    email = models.CharField(max_length=255, default='someone@email.com')
    role = models.CharField(max_length=2, choices=ROLE_CHOICE, default=2)
    age = models.IntegerField(default=3)
    gender = models.BooleanField(default=False)
    memo = models.TextField(default='Memo')
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

from django.db import models

class Users(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=12)
    image = models.ImageField(blank=True, upload_to='users/')
    introduce = models.TextField(blank = True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name_plural = "사용자"
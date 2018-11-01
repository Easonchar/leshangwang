from django.db import models

# Create your models here.
class test(models.Model):
    name = models.CharField(max_length=80)

class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=20)

    token = models.CharField(max_length=256, default='')


class goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=20)
    unit = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    img1 = models.CharField(max_length=256)
    img2 = models.CharField(max_length=256)
    img3 = models.CharField(max_length=256)
    img4 = models.CharField(max_length=256)
    img5 = models.CharField(max_length=256)
    img6 = models.CharField(max_length=256)
    img7 = models.CharField(max_length=256)
    img8 = models.CharField(max_length=256)
    img9 = models.CharField(max_length=256)
    img10 = models.CharField(max_length=256)

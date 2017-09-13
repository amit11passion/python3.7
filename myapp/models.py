from django.db import models


class Uname(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username+' '+self.password


class Udetail(models.Model):
    uname = models.ForeignKey(Uname,on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default = 0)

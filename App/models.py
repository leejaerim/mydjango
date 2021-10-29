from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class User(models.Model):
    uid = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    def __str__(self):
        return '{} {}'.format(self.uid, self.password)
    # def __init__(self,uid,password):
    #     self.uid = uid
    #     self.password = password
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

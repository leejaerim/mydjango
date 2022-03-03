from django.db import models

class User(models.Model):
    uid = models.CharField(unique=True,max_length=12)
    password = models.CharField(max_length=12)
    def __str__(self):
        return '{} {}'.format(self.uid, self.password)
    # def __init__(self,uid,password):
    #     self.uid = uid
    #     self.password = password
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
class Menu(models.Model):
    mid = models.CharField(unique=True,max_length=10,primary_key=True)
    mName = models.CharField(max_length=10)
    mCost = models.IntegerField(default=0)
    def __str__(self):
        return '{} {} {}'.format(self.mid, self.mName,self.mCost)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
class MenuOrder(models.Model):
    sumCost = models.IntegerField(default=0)
    regDate =  models.DateField(auto_now=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
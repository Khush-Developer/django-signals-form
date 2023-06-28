from django.db import models
from django.db.models.signals import pre_delete,post_save
from django.dispatch import receiver

# Create your models here.
class Mymodel(models.Model):
    name= models.CharField(max_length=225)
    description= models.TextField()

def __str__(self):
    return self.name

# create signals.

@receiver(post_save,sender=Mymodel)
def mymodel_post_save(sender,instance,**kwargs):
    print('a model instance saved.')

@receiver(pre_delete,sender=Mymodel)
def mymodel_pre_delete(sender,instance,**kwargs):
    print('a model instance is about delete.')
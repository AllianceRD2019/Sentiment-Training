from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
import os



class Document(models.Model):
    document = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    url= models.CharField(max_length=1000, blank=True, null= True)
    text= models.CharField(max_length=1000, blank=True, null= True)
    desc=models.CharField(max_length=1000, blank=True, null= True)
    label=models.CharField(max_length=1000, blank=True, null= True)
    score=models.CharField(max_length=1000, blank=True, null= True)
    catLabel=models.CharField(max_length=1000, blank=True, null= True)

    conText=models.CharField(max_length=1000, blank=True, null= True)
    conRel=models.CharField(max_length=1000, blank=True, null= True)
    conSource=models.CharField(max_length=1000, blank=True, null= True)
   
    entityText=models.CharField(max_length=1000, blank=True, null= True)
    entityType=models.CharField(max_length=1000, blank=True, null= True)

    mdTitle = models.CharField(max_length=1000, blank=True, null= True)
    mdDate = models.CharField(max_length=1000, blank=True, null= True)



    def __str__(self):
            return "%s (ID:%s)" % (self.name, self.id)
    

















        


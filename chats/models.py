from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

import uuid

# Create your models here.

class model_Chat(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.DateTimeField("Created bt", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField("Delete at", auto_now=True)
    deleted_by = models.DateTimeField("Delete bt", auto_now=True)



class organization(models.Model)   :
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    model_chat = models.ForeignKey(model_Chat,on_delete=models.CASCADE)



class Department(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    organization = models.ForeignKey(organization,on_delete=models.CASCADE)
    model_chat = models.ForeignKey(model_Chat,on_delete=models.CASCADE)

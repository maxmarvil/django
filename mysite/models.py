from django.contrib.auth.models import User
from django.db import models

PREVIEW_LONG = 20

class Category(models.Model):
   name = models.CharField(max_length=100)
   descriptor = models.TextField()
   creator = models.ForeignKey(User)


   def __str__(self):
      return self.name

   def get_preview_text(self):
      if len(self.descriptor) > PREVIEW_LONG:
         return self.descriptor[:PREVIEW_LONG]
      else:
         return self.descriptor
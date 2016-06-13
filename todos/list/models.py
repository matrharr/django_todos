from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
  title = models.CharField(max_length=20)
  body = models.TextField(default='')
  created_at = models.DateTimeField('date published')
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title

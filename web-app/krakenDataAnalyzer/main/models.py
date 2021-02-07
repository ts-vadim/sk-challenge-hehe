from django.db import models
from django.conf import settings
from os import path


class FileModel(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	photo = models.FileField(upload_to='files/')

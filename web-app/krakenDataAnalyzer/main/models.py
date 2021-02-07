from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	photo = models.FileField(upload_to='media/photos/%Y/%m/%d/')

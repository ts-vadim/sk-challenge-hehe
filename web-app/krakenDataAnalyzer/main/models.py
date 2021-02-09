from django.db import models
from django.conf import settings
from os import path


class KrakenRecord(models.Model):
	title = models.CharField(verbose_name='Record Title', max_length=250)
	file = models.FileField(verbose_name='Record File', upload_to=settings.RECORDS_PATH)
	created_at = models.DateTimeField(verbose_name='Date of Creation', auto_now_add=True)

	def __str__(self):
		return self.title


class SiteMember(models.Model):
	name = models.CharField(verbose_name="Member Name", max_length=150)
	about = models.TextField(verbose_name="About Yourself", blank=True)
	contact_url = models.URLField(verbose_name="Contact Url", blank=True)

	def __str__(self):
		return self.name

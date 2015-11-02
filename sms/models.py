from django.db import models
import datetime
from django.utils import timezone


class Product(models.Model):

	name = models.CharField(max_length = 200)
	ptype = models.CharField(max_length = 200)
	entry_date = models.DateTimeField(auto_now=True)
	amount = models.IntegerField()


	def __str__(self):

		return self.name
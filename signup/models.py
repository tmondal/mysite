from django.db import models

# Create your models here.
class Signup(models.Model):
	first_name = models.CharField(max_length = 100,null = True,blank = True)
	last_name = models.CharField(max_length = 100, null = True,blank = True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)


	def __str__(self):
		return self.email
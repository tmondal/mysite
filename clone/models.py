from django.db import models


class People(models.Model):
	pid = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 200)
	gender = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 75)
	dob = models.DateTimeField(auto_now_add = False)
	city = models.CharField(max_length = 200)
	country = models.CharField(max_length = 200)
	#jobtitle = models.CharField(max_length = 200)
	rolename = models.CharField(max_length = 200)

	def __str__(self):
		return self.name
	

class Movie(models.Model):
	mvid = models.AutoField(primary_key = True)
	people = models.ManyToManyField(People)
	title = models.CharField(max_length = 200)
	release = models.DateTimeField()
	country = models.CharField(max_length = 200)
	run_time = models.IntegerField(default = 0)
	language = models.CharField(max_length = 50)
	colour = models.BooleanField(default = True)
	rating = models.IntegerField(default = 0)
	ranking = models.IntegerField(default = 0)
	body = models.TextField(max_length = 200)
	genre = models.CharField(max_length = 100)

	def __str__(self):
		return self.title


class Studio(models.Model):
	sid = models.AutoField(primary_key = True)
	movie = models.OneToOneField(Movie)
	name = models.CharField(max_length = 100)
	establised = models.DateField(auto_now_add = False)
	country = models.CharField(max_length = 20)

	def __str__(self):
		return self.name,self.country
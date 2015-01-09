from django.db import models



# class About(models.Model):

	# 	body = models.TextField()

	# 	def __str__ (self):

	# 		return self.body

	# class Project(models.Model):

	# 	title = models.CharField(max_length = 200)
	# 	body = models.TextField()
	# 	created = models.DateTimeField(auto_now_add = True)

	# 	def __str__ (self):

	# 		return self.title
			

	# class Discuss(models.Model):
	# 	author = models.CharField(max_length = 70)		
	# 	title = models.CharField(max_length = 200)
	# 	field = models.TextField()
	# 	project = models.ForeignKey(Project)

class blogPost(models.Model):

	title = models.CharField(max_length = 200)
	body = models.TextField()
	birth = models.DateTimeField(auto_now_add = True)


	def __str__(self):

		return self.title


class blogComment(models.Model):

	created = models.DateTimeField(auto_now_add = True)
	author = models.CharField(max_length = 200)
	body = models.TextField()
	blogpost = models.ForeignKey(blogPost)


	def __str__(self):

		return self.body[:60]


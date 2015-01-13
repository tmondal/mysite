from django.db import models


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


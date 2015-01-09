from django.contrib import admin
from Myblog.models import blogPost, blogComment


class AdminblogPolst(admin.ModelAdmin):

	display_fields = ["title", "birth"]

class AdminblogComment(admin.ModelAdmin):
	display_fields = ["blogpost", "created", "author"]

admin.site.register(blogPost, AdminblogPolst)
admin.site.register(blogComment ,AdminblogComment)

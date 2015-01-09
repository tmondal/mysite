from django.shortcuts import render
from Myblog.models import blogPost,blogComment



def blogHome(request):

	blogpost = blogPost.objects.all()
	return render(request,'Myblog/blogHome.html', {'blogPost': blogpost})
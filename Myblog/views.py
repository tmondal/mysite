from django.shortcuts import render
from Myblog.models import blogPost,blogComment
from django.views import generic

def blogHome(request):

	blogpost = blogPost.objects.all()
	return render(request,'Myblog/blogHome.html', {'blogpost': blogpost})

def blogDetail(request,blah):
	blog = blogPost.objects.get(pk=blah)
	return render(request, 'Myblog/blogDetail.html', {'post': blog})


from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import RequestContext

from .models import blogPost,blogComment
from .forms import CommentForm

def blogHome(request):

	blogpost = blogPost.objects.all()
	return render(request,'Myblog/blogHome.html', {'blogpost': blogpost})

def blogDetail(request,blah):
	blog = get_object_or_404(blogPost, pk = blah)
	comments = blog.blogcomment_set.all()
	form = CommentForm(request.POST)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.blogpost = blog
		save_it.save()
	return render_to_response('Myblog/blogDetail.html',{'form': form,'blog':blog,'comments':comments},context_instance = RequestContext(request))
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.core.context_processors import csrf
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect

def productHome(request):
	return render(request,'sms/productHome.html');

def productDetails(request):
	return render_to_response('sms/productDetails.html',{
			'products' : Product.objects.all()
		})

def productUpdate(request):
	if request.POST:
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/sms/templates/sms/productdetails/");
		else:
			args = {}
			args.update(csrf(request))
			args['form'] = form
			return render_to_response('sms/productUpdate.html', args)	
	else:
		form = ProductForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
 		
	return render_to_response('sms/productUpdate.html',args)	

def productQuiery(request):
  
    result = []
    if request.method == 'GET': 
        query = request.GET.get('search_box', None)
        product = Product.objects.all()

    return render_to_response('sms/productQuiery.html',{'product':product,'query':query})

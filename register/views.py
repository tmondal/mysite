from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.core.context_processors import csrf


def login(request):
	dic = {}
	dic.update(csrf(request))
	return render_to_response('accounts/login.html',dic)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user is not None:
        # if user.is_active:
        #     login(request,user)
        #     # Redirect to a success page.
        #     return HttpResponseRedirect('logged_in')
        # else:
        #     # Return a 'disabled account' error message
        #     print('The account has been disabled')
        login(request)
        return HttpResponseRedirect('logged_in')
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('invalid_login')

def logged_in(request):
	return render_to_response('accounts/logged_in.html',{'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('accounts/invalid_login.html')

def logout_view(request):
	logout(request)
	return render_to_response('accounts/logout.html')



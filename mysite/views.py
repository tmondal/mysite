from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Choice, Question


# def vote(request,question_id):
# 	p = get_object_or_404(Question, pk = question_id)

#     	try:
#         	selected_choice = p.choice_set.get(pk = request.POST['choice'])
#     	except (KeyError, Choice.DoesNotExist):
        
#         	return render(request, 'polls/detail.html', {'question': p,'error_message': "You didn't select a choice.",})

#     	else:
# 	        selected_choice.votes += 1
# 	        selected_choice.save()
# 	        return HttpResponseRedirect(reverse('polls:results', args = (p.id,)))

def home(request):
	return render(request, 'polls/home.html')


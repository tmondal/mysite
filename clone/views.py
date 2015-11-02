from django.shortcuts import render
from clone.models import People,Movie,Studio

def peopleview(request):

	all_people = People.objects.raw('SELECT * FROM clone_people')
	return render(request,'clone/people.html',{'all_people':all_people})
	

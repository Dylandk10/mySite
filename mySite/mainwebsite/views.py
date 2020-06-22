from django.shortcuts import render
from django.http import HttpResponse
from .databaseManager import Database_Manager
from .models import HighScores

# Function based views
def home(request):
	return render(request, 'mainwebsite/index.html')

def squareWars(request):
	return render(request, 'mainwebsite/game.html')

def contact(request):
	return render(request, 'mainwebsite/contact.html')

def requestHighScore(request):
	value = list(request.GET.values())[0]
	response = Database_Manager.compare(value)
	return HttpResponse(response)

def updateHighScores(request):
	score = list(request.GET.values())[0]
	name = list(request.GET.values())[1]
	Database_Manager.add_highScore(name, score)
	Database_Manager.give_rank()
	return HttpResponse('true')

def highScores(request):
	Database_Manager.give_rank()
	#order by rank so front end doesn't need to order
	content = {
		'model': HighScores.objects.all().order_by('rank')
	}
	return render(request, 'mainwebsite/highScores.html', content)

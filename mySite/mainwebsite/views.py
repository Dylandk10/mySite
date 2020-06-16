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
	database_handler = Database_Manager()
	response = database_handler.compare(value)
	return HttpResponse(response)

def updateHighScores(request):
	score = list(request.GET.values())[0]
	name = list(request.GET.values())[1]
	database_handler = Database_Manager()
	database_handler.add_highScore(name, score)
	return HttpResponse('true')

def highScores(request):
	content = {
		'model': HighScores.objects.all()
	}
	return render(request, 'mainwebsite/highScores.html', content)

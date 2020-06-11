from django.shortcuts import render
from django.http import HttpResponse
from .models import HighScores

# Function based views
def home(request):
	return render(request, 'mainwebsite/index.html')

def squareWars(request):
	return render(request, 'mainwebsite/game.html')

def contact(request):
	return render(request, 'mainwebsite/contact.html')

def requestHighScore(request):
	print(request.GET)
	response = 'true'
	return HttpResponse(response)

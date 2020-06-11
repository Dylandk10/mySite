from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mainpage-home'),
    path('squareWars/', views.squareWars, name='mainpage-squareWars'),
    path('contact/', views.contact, name='mainpage-contact'),
    path('requestHighScore/', views.requestHighScore, name="high-score-request")
]

from django.db import models

# Create your models here.
class HighScores(models.Model):
    name = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score

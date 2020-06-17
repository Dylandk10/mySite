from django.db import models

# Create your models here.
class HighScores(models.Model):
    name = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    rank = models.CharField(max_length=2, default='0')
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    def get_rank(self):
        return self.rank

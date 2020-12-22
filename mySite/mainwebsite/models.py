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

class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=600)
    ip = models.CharField(max_length=100)
    def get_message(self):
        return self.message
    def get_ip(self):
        return self.ip
    def get_email(self):
        return self.email

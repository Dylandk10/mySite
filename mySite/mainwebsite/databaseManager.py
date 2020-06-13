from .models import HighScores

class Database_Manager:
    def __init__(self):
        self.all_entries = HighScores.objects.all()
    def add_highScore(self, user_name, user_score):
        new_entry = HighScores.objects.create(name=user_name, score=user_score)
        HighScore.add(new_entry)
        if self.all_entries.count() > 10:
            #to keep the rows at 10 for only having 10 highscores
            last_entry = HighScores.objects.order_by('score')[11]
            last_entry.delete()

    def compare(self, user_score):
        result = 'false'
        #make a file for me to hold
        if self.all_entries.count() == 0:
            new_entry = HighScores.objects.create(name="Dylan Kelly", score=user_score)
            new_entry.add(new_entry)
            new_entry.save()
        print(self.all_entries.count())
        #if there isnt enough highscores returntrue
        if(self.all_entries.count() <= 10):
            result = 'true'


        for i in self.all_entries:
            if int(user_score) > int(i.get_score()):
                result = 'true'

        return result;
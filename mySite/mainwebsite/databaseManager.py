from .models import HighScores

#Static class no need for instance since this class monitors the database we need to use only the static methods
# if instances are created it can have wrong "threads" and inaccurate data
class Database_Manager:

    def add_highScore(user_name, user_score):
        all_entries = HighScores.objects.all()
        new_entry = HighScores.objects.create(name=user_name, score=user_score)
        new_entry.save()
        if all_entries.count() > 10:
            #to keep the rows at 10 for only having 10 highscores
            last_entry = HighScores.objects.all().order_by('score')[11]
            last_entry.delete()

    def compare(user_score):
        all_entries = HighScores.objects.all()
        result = 'false'
        #make a file for me to hold
        if all_entries.count() == 0:
            new_entry = HighScores.objects.create(name="null", score=user_score)
            new_entry.save()
        print(all_entries.count())
        #if there isnt enough highscores returntrue
        if(all_entries.count() <= 10):
            result = 'true'


        for i in all_entries:
            if int(user_score) > int(i.get_score()):
                result = 'true'

        return result;

    #update the rank of the players before highscores is called to the front end
    def give_rank():
        ordered_highscores = HighScores.objects.all().order_by('score')

        i = ordered_highscores.count()
        for set in ordered_highscores:
            set.rank = i
            i -= 1
            set.save()

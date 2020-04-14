import database
import re

def get_hashtags(text):
    try:
        hashtags = text["entities"]["hashtags"]
        if(len(hashtags)>0):
            hashtags =map(lambda w: (w["text"],1),hashtags)
            database.update_hashtag_count(hashtags)
    except:
        return False
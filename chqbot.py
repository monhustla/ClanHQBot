import praw
import datetime
import time


bot=praw.Reddit(user_agent='MySimpleBot v0.1',
                client_id='tMmbJ410gthhGw',
                client_secret='WREWn4OgA4I3Wl4XVxspVleWDbg',
                username='Clan_HQ',
                password='Bboy123!')

subreddit=bot.subreddit('space')

comments=subreddit.stream.submissions()
keyword=['mars']

def recruiting_check():
  try:
    for comment in comments:
      text=comment.title
      info=comment.created
      nice=datetime.datetime.fromtimestamp(float(info)).isoformat()
      if any(x in text.lower() for x in keyword):
        print(text+'/n'+'/n'+str(nice))
        comment.reply('Mars is awesome')
    time.sleep(60)
            
          
    #author=comments.author
    #if any(x in text.lower() for x in keyword):
    #    print (text+'/n'+'/n'+'yay''/n')

import praw
import datetime
import time
import sched
import psycopg2
import psycopg2.extras
import os
from os import environ
import sys
import urllib.parse as urlparse

bot=praw.Reddit(user_agent='MySimpleBot v0.1',
                client_id='tMmbJ410gthhGw',
                client_secret='WREWn4OgA4I3Wl4XVxspVleWDbg',
                username='Clan_HQ',
                password='Bboy123!')

db_url = os.environ.get('DATABASE_URL', None)
if db_url:
    url = urlparse.urlparse(db_url)
    dbname = url.path[1:]
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port

    conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
                )

subreddit=bot.subreddit('space')

submissions=subreddit.new(limit=1)
#keyword=['mars']

#author=comment.author

#try:
s=sched.scheduler(time.time, time.sleep)
def pullthatshit(sc):
  for submission in submissions:
    person=submission.author
    print(person)
      
    #comment=comment.comments[0]
    
    #person=submission.comments[0].author
        #nice=datetime.datetime.fromtimestamp(float(info)).isoformat()
        
    try:
      cur= None
      cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
      cur.execute("""SELECT username FROM reddit_userinfo WHERE username= %(username)s LIMIT 1""", {"username":person})
      rows=cur.fetchall()
      conn.commit()

      #The user exists in the database and a result was returned
      for row in rows:
        username=row['username']
        print(username)


      else:
        username=person

    except BaseException as e:
      print (e)
      if cur is not None:
        conn.rollback()
        print("Something is wrong")
        cur.close()

    finally:
      if cur is not None:
        conn.commit()
        print("Something is wrong 2")
        cur.close()
            
        
        username=person
        
        info_one="Whatever"
        
        info_two="Whatever"
        
        info_three="Whatever"
        
        info_four="Whatever"
        
        info_five="Whatever"
        
        try:
          cur= None
          cur= conn.cursor()
          cur.execute("""INSERT INTO reddit_userinfo(username, info_one, info_two, info_three, info_four, info_five)
                          VALUES(%(username)s, %(info_one)s, %(info_two)s, %(info_three)s, %(info_four)s, %(info_five)s)""")
                          
          conn.commit()
          print("you got it bud")
        
        except BaseException:
          if cur is not None:
            conn.rollback()
            cur.close()
            return
         
        finally:
          if cur is not None:
            cur.close()
        return    
        
    #if any(x in text.lower() for x in keyword):
        #print(text+'\n'+'\n'+str(nice)+'\n'+person)
            #comment.reply('Mars is awesome')
        #time.sleep(60)
    s.enter(5,1, pullthatshit, (sc,))
s.enter(80, 1, pullthatshit, (s,))
s.run()
#except:
#    print ('This did not work')
    #author=comments.author
    #if any(x in text.lower() for x in keyword):
    #    print (text+'/n'+'/n'+'yay''/n')

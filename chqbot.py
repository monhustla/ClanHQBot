from __future__ import unicode_literals
import praw
import datetime
import time
import schedule
import psycopg2
import psycopg2.extras
import os
from os import environ
import sys
import urllib.parse as urlparse
from flask import Flask, request, abort


app = Flask(__name__)

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
#s=sched.scheduler(time.time, time.sleep)
def pullthatshit():
  for submission in submissions:
    person=str(submission.author)
    print(person+"ok")
      
    #comment=comment.comments[0]
    
    #person=submission.comments[0].author
        #nice=datetime.datetime.fromtimestamp(float(info)).isoformat()

    try:
      cur= None
      cur= conn.cursor()
      cur.execute("""SELECT username FROM reddit_userinfo WHERE username= %(username)s LIMIT 1""", {"username":person})
      rows=cur.fetchall()
      print(rows)
      conn.commit()
      for row in rows:
        dude1=rows[0]
        
        dude=str(dude1).replace("'","").replace("(","").replace(")","").replace(",","")
        print("Here is your dude: "+ dude)
        print("Here is your person: "+ person)
        if dude==person:
          print ("This person exists, exiting")
        return True  
          
    except (BaseException, IndexError) as e:
      print ("Index Error")
      if cur is not None:
        conn.rollback()
        print(e+"Something is wrong")
        cur.close()
      continue  

    finally:
      if cur is not None:
        conn.commit()
        cur.close()
        
                  
          
        
                  
                  
     

      #The user exists in the database and a result was returned
      #for row in rows:
      #  username=row[0]
      #  print(username)


      #else:
      #  username=person

    print("This is a new person, adding them to the database")
        
    username=person

    info_one="Whatever"

    info_two="Whatever"

    info_three="Whatever"

    info_four="Whatever"

    info_five="Whatever"

    try:
      cur= None
      cur= conn.cursor()
      cur.execute("""INSERT INTO reddit_userinfo (username, info_one, info_two, info_three, info_four, info_five)
                     VALUES (%s, %s, %s, %s, %s, %s)""",
                     (person, info_one, info_two, info_three, info_four, info_five))

      conn.commit()
      print("you got it bud")
      #time.sleep(.4)
      

    except BaseException as e:
      if cur is not None:
        print(e+"Insert did not work")
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
  #s.enter(5,1, pullthatshit, (sc,))
#s.enter(80, 1, pullthatshit, (s,))
#s.run()


schedule.every(.2).minutes.do(pullthatshit)
  return
while 1:
  schedule.run_pending()
  time.sleep(.4)
  return

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
#except:
#    print ('This did not work')
    #author=comments.author
    #if any(x in text.lower() for x in keyword):
    #    print (text+'/n'+'/n'+'yay''/n')

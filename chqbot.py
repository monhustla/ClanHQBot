import praw
import datetime
import time
import sched

bot=praw.Reddit(user_agent='MySimpleBot v0.1',
                client_id='tMmbJ410gthhGw',
                client_secret='WREWn4OgA4I3Wl4XVxspVleWDbg',
                username='Clan_HQ',
                password='Bboy123!')

subreddit=bot.subreddit('space')

submission=subreddit.stream.submissions()
#keyword=['mars']
#comment=submission.comments[0]
#author=comment.author

#try:
s=sched.scheduler(time.time, time.sleep)
def pullthatshit(sc):
    for comment in submission:
        text=comment.title
        info=comment.created
        person=comment.author.name
    #comment=comment.comments[0]
    
    #person=submission.comments[0].author
        nice=datetime.datetime.fromtimestamp(float(info)).isoformat()
        print(text+'\n'+'\n'+str(nice)+'\n'+person)
    #if any(x in text.lower() for x in keyword):
        #print(text+'\n'+'\n'+str(nice)+'\n'+person)
            #comment.reply('Mars is awesome')
        #time.sleep(60)
    s.enter(10,1, pullthatshit, (sc,))
s.enter(80, 1, pullthatshit, (s,))
s.run()
#except:
#    print ('This did not work')
    #author=comments.author
    #if any(x in text.lower() for x in keyword):
    #    print (text+'/n'+'/n'+'yay''/n')

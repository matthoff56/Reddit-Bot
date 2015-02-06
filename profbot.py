#Matt Stierhoff
#profanity reddit bot

import praw
import time
import re
r = praw.Reddit(user_agent='profanity_bot')
r.login('Profanity-bot', 'Robotpass5')
#r.send_message('space_broccoli', 'test', 'test')

foulLang = [' ass ', 'asshole', 'bastard', 'bitch', 'cock', 'damn', 'fuck', 'goddamn', 'holy shit', 'motherfucker', 'pussy', 'shit', 'testswear']

file = open('postids.txt', 'r')
already_done = set()
for line in file:
        already_done.add(line)
file.close()

while True:
        #submissions = r.get_subreddit('umw_cpsc470Z').get_hot(limit=10)
        subreddit = r.get_subreddit('umw_cpsc470Z')
        for submission in subreddit.get_hot(limit=10):
                flat_comments = praw.helpers.flatten_tree(submission.comments)
                for comment in flat_comments:
                        op_text = comment.body.lower()
                        for i in foulLang:
                                if i in op_text and comment.id not in already_done:
                                        print i
                                        comment.reply('http://youtu.be/YR9UL1Cqpxw')
                                        file = open("postids.txt", "w")
                                        file.write("%s\n" % comment.id)
                                        file.close()
                                        already_done.add(comment.id)
                                        time.sleep(1000)



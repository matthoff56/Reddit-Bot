#Matt Stierhoff
#profanity reddit bot

import praw
import time
r = praw.Reddit(user_agent='profanity_bot')
r.login('Profanity-bot', 'Robotpass5')
#r.send_message('space_broccoli', 'test', 'test')

foulLang = ['ass', 'asshole', 'bastard', 'bitch', 'cock', 'damn', 'fuck', 'goddamn', 'holy shit', 'motherfucker', 'pussy', 'shit', 'testswear']
already_done = set()

while True:
        #submissions = r.get_subreddit('umw_cpsc470Z').get_hot(limit=10)
        subreddit = r.get_subreddit('umw_cpsc470Z')
        for submission in subreddit.get_hot(limit=10):
                flat_comments = praw.helpers.flatten_tree(submission.comments)
                for comment in flat_comments:
                        op_text = comment.body.lower()
                        has_swear = any(string in op_text for string in foulLang)
                        if has_swear and comment.id not in already_done:
                                comment.reply('http://youtu.be/YR9UL1Cqpxw')
                                already_done.add(comment.id)
                                time.sleep(1000)
        #time.sleep(2000)

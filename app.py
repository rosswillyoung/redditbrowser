import praw
import pprint

             
for submission in reddit.subreddit('reddevils').hot(limit=1):
    print(submission.title)
    pprint.pprint(vars(submission))

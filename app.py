import pprint
import json
import praw
             
with open('keys.json') as f:
    data = json.load(f)
    client_id = data["data"]["client_id"]
    client_secret = data["data"]["client_secret"]
    user_agent = data["data"]["user_agent"]

print(user_agent)

# for submission in reddit.subreddit('reddevils').hot(limit=1):
#     print(submission.title)
#     pprint.pprint(vars(submission))

import pprint
import json
import praw
import os
             
# Get PRAW client information from keys.json file
with open('keys.json') as f:
    data = json.load(f)
    client_id = data["data"]["client_id"]
    client_secret = data["data"]["client_secret"]
    user_agent = data["data"]["user_agent"]

# Connect to PRAW with client information
reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent)

# Gets comments from a submission
def get_comments(submission):
    for top_level_comment in submission.comments:
        print(top_level_comment.body)
        print('~~~~~~~~~~~~~~~~~~~~~~')
        second_level = input("Get second level comments? ")
        if (second_level == "Y" or second_level == "y"):
            for second_level_comment in top_level_comment.replies:
                print(second_level_comment.body)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif (second_level == "quit" or second_level == "Quit"):
            break
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            next


def get_submissions(sub, sort_by):
    if sort_by == "hot" or sort_by == "Hot":
        for submission in reddit.subreddit(sub).hot(limit=10):
            print(submission.title)
            print('')
            print(submission.selftext)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            user_wants_comments = input("Load Comments? (y/Y for yes) ")
            if (user_wants_comments == "y" or user_wants_comments == "Y"):
                get_comments(submission)
            elif(user_wants_comments == "quit" or user_wants_comments == "Quit"):
                break
            else:
                next
            print("Loading next title...")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            # pprint.pprint(vars(submission))
    elif sort_by == "top" or sort_by == "Top":
        sort_by_time = input("Do you want the top posts of the day/week/month/year or all time?" +
        "Please enter 'day', 'week', 'month', 'year', or 'all' ")
        os.system('cls')
        for submission in reddit.subreddit(sub).top(sort_by_time, limit=10):
            print(submission.title)
            print('')
            print(submission.selftext)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            user_wants_comments = input("Load Comments? (y/Y for yes) ")
            if (user_wants_comments == "y" or user_wants_comments == "Y"):
                get_comments(submission)
            elif(user_wants_comments == "quit" or user_wants_comments == "Quit"):
                break
            else:
                next
            print("Loading next title...")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            # pprint.pprint(vars(submission))

sub = input("Which subreddit would you like to view? ")
sort_by = input("Hot or Top? ")
os.system('cls')
get_submissions(sub, sort_by)


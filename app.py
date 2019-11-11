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
        print('###############################################################################')
        print('')
        second_level = input("Get second level comments? ")
        if (second_level == "Y" or second_level == "y"):
            for second_level_comment in top_level_comment.replies:
                print(second_level_comment.body)
                print('###############################################################################')
                print('')
        elif (second_level == "quit" or second_level == "Quit"
                or second_level == "no" or second_level == "No"):
            break
        else:
            print('###############################################################################')
            print('')
            next

    print("Last Comment, loading next post...")
    print('###############################################################################')
    print('')


def get_submissions():
    while True:
        sub = input("Which subreddit would you like to view? ")
        if sub == '':
            print('Please enter a valid subreddit')
            sub = input("Which subreddit would you like to view? ")
        else:
            break
    while True:
        try:
            post_limit = int(input("How many posts would you like to load? "))
            break
        except ValueError:
            print('Please enter a valid number')
    while True:
        sort_by = input("Hot or Top? ")
        if sort_by == '':
            print('Please enter a valid value')
            sort_by = input("Hot or Top? ")
        else:
            break
    if sort_by == "hot" or sort_by == "Hot":
        for submission in reddit.subreddit(sub).hot(limit=post_limit):
            print(submission.title)
            print('')
            print(submission.selftext)
            print('###############################################################################')
            print('')
            user_wants_comments = input("Load Comments? (y/Y for yes) ")
            if (user_wants_comments == "y" or user_wants_comments == "Y" or
                user_wants_comments == "yes" or user_wants_comments == "Yes"):
                get_comments(submission)
            elif(user_wants_comments == "quit" or user_wants_comments == "Quit"):
                break
            else:
                next
            print("Loading next title...")
            print('###############################################################################')
            print('')
            # pprint.pprint(vars(submission))
    elif sort_by == "top" or sort_by == "Top":
        sort_by_time = input("Do you want the top posts of the day/week/month/year or all time?" +
        "Please enter 'day', 'week', 'month', 'year', or 'all' ")
        os.system('cls')
        for submission in reddit.subreddit(sub).top(sort_by_time, limit=post_limit):
            print(submission.title)
            print('')
            print(submission.selftext)
            print('###############################################################################')
            print('')
            user_wants_comments = input("Load Comments? (y/Y for yes) ")
            if (user_wants_comments == "y" or user_wants_comments == "Y" or 
                user_wants_comments == "yes" or user_wants_comments == "Yes"):
                get_comments(submission)
            elif(user_wants_comments == "quit" or user_wants_comments == "Quit"):
                break
            else:
                next
            print("Loading next title...")
            print('###############################################################################')
            print('')
            # pprint.pprint(vars(submission))

os.system('cls')
get_submissions()


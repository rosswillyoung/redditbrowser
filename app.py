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
                    
yes_responses = ['Yes', 'yes', 'Y', 'y']

no_responses = ['No', 'no', 'N', 'n', 'Quit', 'quit', 'Q', 'q']

# Gets comments from a submission
def get_comments(submission):
    for top_level_comment in submission.comments:
        print(top_level_comment.body)
        print('###############################################################################')
        print('')
        second_level = input("Get second level comments? ")
        if (second_level in yes_responses):
            for second_level_comment in top_level_comment.replies:
                try:
                    print(second_level_comment.body)
                    print('###############################################################################')
                    print('')
                except AttributeError:
                    print('No more second-level comments, next top-level comment:')
                    continue
        elif (second_level in no_responses):
            break
        else:
            print('###############################################################################')
            print('')
            next

    print("Last Comment, loading next post...")
    print('###############################################################################')
    print('')

def get_submissions(sub, post_limit, sort_by):
    if sort_by == "hot" or sort_by == "Hot":
        for submission in reddit.subreddit(sub).hot(limit=post_limit):
            print(submission.title)
            print('')
            print(submission.selftext)
            print('###############################################################################')
            print('')
            user_wants_comments = input("Load Comments? (y/Y for yes) ")
            if (user_wants_comments in yes_responses):
                get_comments(submission)
            elif(user_wants_comments in no_responses):
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
            if (user_wants_comments in yes_responses):
                get_comments(submission)
            elif(user_wants_comments in no_responses):
                break
            else:
                next
            print("Loading next title...")
            print('###############################################################################')
            print('')
            # pprint.pprint(vars(submission))

def get_user_input():
    while True:
        sub = input("Which subreddit would you like to view? ")
        if sub == '':
            print('Please enter a valid subreddit')
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
        valid_responses = ['Hot', 'hot', 'Top', 'top', '']
        if sort_by not in valid_responses:
            print('Please enter a valid value')
        else:
            break
    get_submissions(sub, post_limit, sort_by)

os.system('cls')
while True:
    load_subreddit = input("Load a subreddit? ")
    if load_subreddit in yes_responses or load_subreddit == '':
        get_user_input()
    else:
        break


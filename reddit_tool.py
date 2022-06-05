import praw
import random
import os, re

CHAR_LIMIT = 219 # burası yorum en fazla kaç char olabilir

def remove_url(string):
    text = re.sub("(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*", "", string)
    return text

def get_subreddit_threads(id, secret, username, password, subreddit_limit, sub_number, sub_name):
    print("Getting AskReddit threads...")
    reddit = praw.Reddit(
        client_id= id,
        client_secret=secret,
        user_agent="Accessing AskReddit threads",
        username=username,
        password=password
    )
    subreddit = reddit.subreddit(sub_name)
    
    threads = subreddit.hot(limit=subreddit_limit)
    submission = list(threads)[sub_number] 

    print(f"Videoyu şundan yapıyom ona göre: {submission.title}")

    content = {}

    try:
        content["thread_url"] = submission.url
        content["thread_title"] = submission.title
        content["comments"] = []

        for top_level_comment in submission.comments:
            if (top_level_comment.author != "AutoModerator"):
                if len(top_level_comment.body) <= CHAR_LIMIT:
                    _comment_text = remove_url(top_level_comment.body)
                    content["comments"].append(
                        {
                            "comment_body": _comment_text,
                            "comment_url": top_level_comment.permalink,
                            "comment_id": top_level_comment.id,
                        }
                    )
            else:
                print("AutoModerator yorumu geçildi..")

    except AttributeError as e:
        pass

    print("başarıyla AskReddit yorumlarını çaldık..")

    return content

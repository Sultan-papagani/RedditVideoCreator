import praw
import random
import os, re

def get_threads_names(id, secret, username, password, subreddit_limit, sub_name):
    print(f"ilk {subreddit_limit}. post alınıyor ( OK = Yorum başına Ortalama Karakter Sayısı)")
    reddit = praw.Reddit(
        client_id= id,
        client_secret=secret,
        user_agent="Accessing AskReddit threads",
        username=username,
        password=password
    )
    subreddit = reddit.subreddit(sub_name)
    
    threads = subreddit.hot(limit=subreddit_limit)
    for index, th in enumerate(list(threads)):
        ortalama_char = 0
        i = 0
        for comment in th.comments:
            if (comment.author != "AutoModerator"):
                ortalama_char += len(comment.body)
                i += 1
            if i >= 10: break
        ortalama_char /= 10
        nsfw = ""
        if th.over_18:
            nsfw = "NSFW"
        print(f"{index} | {th.title} | OK:{ortalama_char} | {nsfw}")

    del(reddit)

from random import randint
import reddit_tool
import youtube_tool
import screenshot_downloader
import background
import final_video

REDDIT_CLIENT_ID=""               
REDDIT_CLIENT_SECRET=""   
REDDIT_USERNAME=""       #hesabınızın adı
REDDIT_PASSWORD=""    #hesap şifresi
REDDIT_2FA=""   
THEME="dark"

SUBREDDIT_LIMIT_THREAD = 25
SUB_NUMBER = randint(1, 10)
SUB_NAME = "askreddit"


print("redditden otomatik aptal videolar oluşturma aracına hoş gelmediniz")


reddit_object = reddit_tool.get_subreddit_threads(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
                                                 REDDIT_USERNAME, REDDIT_PASSWORD, SUBREDDIT_LIMIT_THREAD, 
                                                 SUB_NUMBER, SUB_NAME)

length, number_of_comments = youtube_tool.save_text_to_mp3(reddit_object)

print(f"length: {length} comment count: {number_of_comments}")

screenshot_downloader.download_screenshots_of_reddit_posts(
                      reddit_object, number_of_comments, THEME)

background.download_background()
background.chop_background_video(length)
video = final_video.make_final_video(number_of_comments)


from random import randint
import reddit_tool
import youtube_tool
import screenshot_downloader
import background
import final_video
import print_threads

REDDIT_CLIENT_ID=""               
REDDIT_CLIENT_SECRET=""   
REDDIT_USERNAME=""       #hesabınızın adı
REDDIT_PASSWORD=""    #hesap şifresi
REDDIT_2FA=""   
THEME="dark"

SUBREDDIT_LIMIT_THREAD = 25
SUB_NUMBER = 5 # "5" sadece duruyor seçimi sana soruyo ztn
SUB_NAME = "askreddit"

CHAR_LIMIT = 320 #319
VIDEO_LENGTH_MAX = 45


print("Reddit'den otomatik video oluşturma aracına hoş geldiniz")

print("Postlar listelensin mi? (y/n)")
secim = input()
if secim == "y":
    print_threads.get_threads_names(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
                                    REDDIT_USERNAME, REDDIT_PASSWORD, SUBREDDIT_LIMIT_THREAD, SUB_NAME)

print("Beğendiniz postun numarasını seçin numarası seçin, Rastgele seçim için boş geçin")
deger = input()

if (deger == ""):
    print("rastgele seçim yapılıyor...")
    SUB_NUMBER = randint(0, SUBREDDIT_LIMIT_THREAD - 1)
SUB_NUMBER = int(deger)

reddit_object = reddit_tool.get_subreddit_threads(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
                                                 REDDIT_USERNAME, REDDIT_PASSWORD, SUBREDDIT_LIMIT_THREAD, 
                                                 SUB_NUMBER, SUB_NAME, CHAR_LIMIT)

length, number_of_comments = youtube_tool.save_text_to_mp3(reddit_object, VIDEO_LENGTH_MAX)

print(f"Son Video Uzunluğu: {length} | Toplam yorum sayısı: {number_of_comments}")

screenshot_downloader.download_screenshots_of_reddit_posts(
                      reddit_object, number_of_comments, THEME)

background.download_background()
background.chop_background_video(length)
video = final_video.make_final_video(number_of_comments)


from pathlib import Path
from rich.progress import track
import json
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from time import sleep

#chromedriver.exe pathını ekleyin
sys.path.append("C:/Users/bişeyler/bişeyler/chromedriver.exe")


def download_screenshots_of_reddit_posts(reddit_object, screenshot_num, theme):
    print("Reddit yorumlarının ekran görüntüleri alınıyor...")

    Path("assets/png").mkdir(parents=True, exist_ok=True)

    print("Görünmez Tarayıcı Başlatıldı...")

    # bu kısma cookie.json dosyasının pathını koyun
    cookie_file = open('C:/Users/bişeyler/bişeyler/cookies.json')
    cookies = json.load(cookie_file)

    options = Options()
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu') 
    options.add_argument("--log-level=3")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    browser = webdriver.Chrome(chrome_options=options)

    browser.get(reddit_object["thread_url"])
    browser.set_window_size(1920, 1080)
    browser.add_cookie(cookie_dict=cookies)


    if browser.find_element_by_xpath('//div[@data-testid="content-gate"]').is_displayed:
            print("Bu post NSFW. seni kirli adam")
            browser.find_element_by_xpath("//button[text()='Yes']").click()
            
    nsfw_spoiler = browser.find_element_by_xpath("//button[text()='Click to see nsfw']")
    if nsfw_spoiler.is_displayed: nsfw_spoiler.click()

    browser.find_element_by_xpath('//div[@data-test-id="post-content"]').screenshot(filename="assets/png/title.png")

    for idx, comment in track(
            enumerate(reddit_object["comments"]), "Downloading screenshots..."
        ):

            # Stop if we have reached the screenshot_num
            if idx >= screenshot_num:
                break

            browser.get(f'https://reddit.com{comment["comment_url"]}')
            browser.find_element_by_css_selector(f"#t1_{comment['comment_id']}").screenshot(filename=f"assets/png/comment_{idx}.png")
    
    print("Ekran görüntüleri başarıyla kaydedildi.")

    browser.close()
    return 

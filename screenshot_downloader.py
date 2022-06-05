from pathlib import Path
from rich.progress import track
import json
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

sys.path.append("C:/Users/bişeyler/bişeyler/chromedriver.exe") #chromedriver indirmen lazım 5mb falan hardpathla işte .exeye


def download_screenshots_of_reddit_posts(reddit_object, screenshot_num, theme):
    print("Downloading Screenshots of Reddit Posts 📷")

    Path("assets/png").mkdir(parents=True, exist_ok=True)

    print("Launching Headless Browser...")

    # bu kısma cookie.json dosyasının pathını koyun
    cookie_file = open('C:/Users/bişeyler/bişeyler/cookies.json') # orjinal bottaki cookies.json hardpatla
    cookies = json.load(cookie_file)

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary
    options.add_argument("--log-level=3")

    browser = webdriver.Chrome(chrome_options=options)

    browser.get(reddit_object["thread_url"])
    browser.set_window_size(1920, 1080)
    browser.add_cookie(cookie_dict=cookies)

    """if browser.find_element_by_id('[data-testid="content-gate"]').is_displayed:
            # This means the post is NSFW and requires to click the proceed button.

            print("Post is NSFW. You are spicy...")
            browser.find_element_by_id('[data-testid="content-gate"] button').click()"""

    browser.find_element_by_xpath('//div[@data-test-id="post-content"]').screenshot(filename="assets/png/title.png")

    for idx, comment in track(
            enumerate(reddit_object["comments"]), "Downloading screenshots..."
        ):

            # Stop if we have reached the screenshot_num
            if idx >= screenshot_num:
                break
            
            #if browser.find_element_by_xpath('//div[@data-testid="content-gate"]').is_displayed:
            #    browser.find_element_by_xpath('//button[@data-testid="content-gate"] button').click()
            browser.get(f'https://reddit.com{comment["comment_url"]}')
            browser.find_element_by_css_selector(f"#t1_{comment['comment_id']}").screenshot(filename=f"assets/png/comment_{idx}.png")
    print("Screenshots downloaded Successfully.")

    return 1

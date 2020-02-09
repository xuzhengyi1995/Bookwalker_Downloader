import base64
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# --------------Settings--------------
# The manga URL that in '購入済み書籍一覧', 'Your manga name', 'この本を読む' button
# Right click the 'この本を読む' and click the 'Copy link address'
MANGA_URL = 'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/640c0ddd-896c-4881-945f-ad5ce9a070a6/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F'
# Your cookies
# Go to this url: https://member.bookwalker.jp/app/03/my/profile, and copy the cookies.
COOKIES = 'YOUR_COOKIES_HERE'
# Folder name, where to put the images
IMGDIR = "./TEST"
# Resolution, this manga is 784*1200, you can change it as you want, but check the original image resolution first.
RES = (784, 1200)
# If your network is good, you can change it to 1 second, this is the time to load next page.
SLEEP_TIME = 2
# Use manual login, if this is true, no need to add cookies.
MANUAL_LOGIN = False
# Time wait to load first page
LOADING_WAIT_TIME = 20
# Keep True, or there will be a 403 error
DEBUG = True
# --------------Settings--------------

if not os.path.isdir(IMGDIR):
    os.mkdir(IMGDIR)


def get_driver():
    option = webdriver.ChromeOptions()
    option.add_argument('--high-dpi-support=1')
    option.add_argument('--force-device-scale-factor=1')
    if not DEBUG:
        option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    return driver


def get_cookie_dict(cookies):
    cookies = cookies.split('; ')
    cookies_dict = {}
    for i in cookies:
        kv = i.split('=')
        cookies_dict[kv[0]] = kv[1]
    return cookies_dict


def add_cookies(driver, cookies):
    for i in cookies:
        driver.add_cookie({'name': i, 'value': cookies[i]})


def login(driver, email, password):
    driver.get('https://member.bookwalker.jp/app/03/login')
    driver.find_element_by_id('mailAddress').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_name('loginBtn').click()


def check_is_loading(list_ele):
    is_loading = False
    for i in list_ele:
        if i.is_displayed() is True:
            is_loading = True
            break
    return is_loading


def main():
    driver = get_driver()
    driver.get('https://member.bookwalker.jp/app/03/login')
    if not MANUAL_LOGIN:
        driver.delete_all_cookies()
        add_cookies(driver, get_cookie_dict(COOKIES))
    else:
        print('Please login...')
        WebDriverWait(driver, 120).until_not(
            lambda x: x.find_elements_by_css_selector('#password'))
        print('Login successfully, please wait...')
    driver.set_window_size(RES[0] + 16, RES[1] + 131)
    driver.get(MANGA_URL)
    print('Preparing for downloading...')
    time.sleep(LOADING_WAIT_TIME)
    try:
        page_count = int(str(driver.find_element_by_id(
            'pageSliderCounter').text).split('/')[1])
        for i in range(page_count):
            WebDriverWait(driver, 30).until_not(lambda x: check_is_loading(
                x.find_elements_by_css_selector(".loading")))
            canvas = driver.find_element_by_css_selector(
                ".currentScreen canvas")
            img_base64 = driver.execute_script(
                "return arguments[0].toDataURL('image/jpeg').substring(22);", canvas)
            with open(IMGDIR + '/%d.jpg' % i, 'wb') as f:
                f.write(base64.b64decode(img_base64))
                print('Page %s Downloaded' % str(i + 1))
                if i == page_count - 1:
                    print('Finished.')
                    break

            next_page = driver.find_element_by_css_selector("#renderer")
            webdriver.ActionChains(driver).move_to_element(
                next_page).click().send_keys(Keys.ARROW_LEFT).perform()
            WebDriverWait(driver, 30).until_not(lambda x: int(
                str(driver.find_element_by_id('pageSliderCounter').text).split('/')[0]) == i + 1)
            time.sleep(SLEEP_TIME)
    except:
        driver.save_screenshot('./error.png')
        print('Something wrong or download finished, Please check the error.png to see the web page.')
        print('Normally, you should logout and login, then renew the cookies to solve this problem.')


if __name__ == '__main__':
    main()

# Bookwalker_Downloader

**Please check [Manga_downloader](https://github.com/xuzhengyi1995/Manga_downloader), it has the same or even more function, Bookwalker_Downloader may no longer be maintained. Thank you.**

**还请尽量使用新版的[Manga_downloader](https://github.com/xuzhengyi1995/Manga_downloader),该程序拥有相同甚至更多功能，Bookwalker_Downloader可能不会再进行维护。谢谢。**

Download manga you rent from <https://bookwalker.jp/>

# How to Use

**No need to find anything on the webpage, just put the cookie and url is ready for use.**

**This program now work for Chrome, if you use another browser, please check [this page](https://selenium-python.readthedocs.io/installation.html)**

0.  Install python packages _selenium_ and get the _Google chrome Drivers_.

    1.  For _selenuim_:

    ```shell
    pip install selenium
    ```

    2.  For Google chrome Drivers:

        1.  Please check your Chrome version, 'Help'->'About Google Chrome'.

        2.  Download Chrome Driver fit to your Chrome version [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

        3.  Put it into any folder and add the folder into the PATH.

    3.  For more info, I suggest you to check it [here](https://selenium-python.readthedocs.io/installation.html)


1.  Change the `IMGDIR` in the main.py to indicate where to put the manga.

2.  Add your cookies in the program.

    **Remember to use F12 to see the cookies!**

    **Because some http only cookies can not be seen by javascript!**

    **Remember to go [here](https://member.bookwalker.jp/app/03/my/profile) to get the cookies!**

    > 1.  Open the page.
    > 2.  Press F12.
    > 3.  Click on the _Network_.
    > 4.  Refresh the page.
    > 5.  Find the first _profile_ request, click it.
    > 6.  On the right, there will be a _Request Headers_, go there.
    > 7.  Find the _cookie:...._, copy the string after the _cookie:_, paste to the _main.py_, _YOUR_COOKIES_HERE_

3.  Change the _url_ in the _main.py_.

    First go to [購入済み書籍一覧](https://bookwalker.jp/holdBooks/), you can find all your mangas here.

    This time the URL is the URL of **'この本を読む'** button for your manga.

    Right click this button, and click **'Copy link address'**.

    The URL is start with **member.bookwalker.jp**, not the **viewer.bookwalker.jp**. Here we use the manga [【期間限定　無料お試し版】あつまれ！ふしぎ研究部　１](https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/640c0ddd-896c-4881-945f-ad5ce9a070a6/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F).

    This is the URL of the **あつまれ！ふしぎ研究部　１**: <https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/640c0ddd-896c-4881-945f-ad5ce9a070a6/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F>

    Just copy this URL to the `MANGA_URL` in _main.py_.

4.  After edit the program, run `python main.py` to run it.

# Notice

1.  The `SLEEP_TIME` by default is 2 seconds, you can adjust it with your own network situation, if the downloading has repeated images, you can change it to 5 or more. If you think it's too slow, try change it to 1 or even 0.5.

2.  Keep the `DEBUG = False`, now it works with headless Chrome after changing the `User-Agent`.

3.  ~~if you want to login manually, please set the `MANUAL_LOGIN = True`, and input the email and password, click the login button. Then the program will detect you have login and continue running.~~

    **Now with headless Chrome, we can only login with cookies.**

4.  `LOADING_WAIT_TIME = 20`, this is the time to wait until the manga viewer page loaded, if your network is not good, you can set it to 30 or 50 seconds.

5.  Resolution, you can change it as you want, but check the original image resolution first.

    ```python
    RES = (784, 1200)
    ```

    If the original image has a higher resolution, you can change it like this (The resolution is just a example).

    ```python
    RES = (1568, 2400)
    ```

6.  Some time we should log out and log in, this website is very strict and take so many method to prevent abuse.

7.  Now you can cut the image by setting `CUT_IMAGE` at line 35 to (left, upper, right, lower).

    For example you want to cut 3px from the bottom of image, you can set it to:

    ```python
    CUT_IMAGE = (0, 0, 0, 3)
    ```

    This function use `Pillow`, if you want to use it, you should install it by using the command:

    ```shell
    pip install Pillow
    ```

    By default it is `None`, means do not cut the image, and no need to install `Pillow`.

# 关于中文站点

中文站点为：<https://www.bookwalker.com.tw>

1.  可用于中文站点，`MANGA_URL`为[线上阅读](https://www.bookwalker.com.tw/member/available_book_list)页面的“阅读”按钮，一般URL类似：<https://www.bookwalker.com.tw/browserViewer/56994/read>

2.  `COOKIES`请前往[个人专页](https://www.bookwalker.com.tw/member)，按照上述方法复制COOKIES。

3.  `RES`的寻找方法相同，中文站点部分漫画分辨率较高，例如[小邪神飞踢](https://www.bookwalker.com.tw/browserViewer/56994/read)的原始分辨率为`RES = (1393, 2048)`。

4.  如果出现 **【The eBook chosen cannot be viewed. Please sign-out, then sign-in again. (ERROR998)】** ，还请使用浏览器先退出登陆，再次登陆，并使用浏览器确认该漫画可正常浏览后，更新Cookies再试。

5.  如果出现 **【The eBook chosen cannot open since not yet purchaesd. Please make a purchase and try again.】** , 还请先确认是否已经购买该漫画，再确认Cookies的获取是否为使用`F12`获取，请不要使用JavaScript获取Cookies，因为部分重要Cookies会被设置为http only，这部分Cookies是无法用JavaScript获取到的。

# Bookwalker_Downloader

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

2.  Keep the `DEBUG = True`, now this website not work with headless Chrome.

3.  Resolution, you can change it as you want, but check the original image resolution first.

    ```python
    RES = (784, 1200)
    ```

    If the original image has a higher resolution, you can change it like this (The resolution is just a example).

    ```python
    RES = (1568, 2400)
    ```

4.  Some time we should log out and log in, this website is very strict and take so many method to prevent abuse.

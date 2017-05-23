import scraperwiki
from time import sleep
from splinter import Browser
from selenium import webdriver


with Browser('phantomjs') as browser:
    # Visit URL
    url = "https://www.google.rs/search?q=bitcoin&tbm=nws&cad=h"
    browser.visit(url)
    sleep(2)

    titles = browser.find_by_xpath('//*[@class="l _PMs"]')
    times = browser.find_by_xpath('//*[@class="f nsa _QHs"]')
    urls = browser.find_by_xpath('//*[@class="top _xGs _SHs"]')
    for title, time, url in zip(titles, times, urls):
        print '-' * 60
        print title.text
        print time.text
        print url['href']
        print '-' * 60
        print '\n'

        scraperwiki.sqlite.save(data={'title': title.text,
                                      'time': time.text,
                                      'url': url['href']})

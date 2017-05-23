# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

from selenium import webdriver
import scraperwiki
from time import sleep
from splinter import Browser

import platform
print platform.platform()

print 'fooobar'

# Read in a page
html = scraperwiki.scrape("http://foo.com")


# Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")

with Browser("phantomjs") as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnG')
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "some name", "occupation": "software"})

# An arbitrary query against the database
scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

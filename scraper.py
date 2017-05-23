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
    # Optional, but make sure large enough that responsive pages don't
    # hide elements on you...
    browser.driver.set_window_size(1280, 1024)

    # Open the page you want...
    browser.visit("https://morph.io")

    # submit the search form...
    browser.fill("q", "parliament")
    button = browser.find_by_css("button[type='submit']")
    button.click()

    # Scrape the data you like...
    links = browser.find_by_css(".search-results .list-group-item")
    for link in links:
        print link['href']

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "some name", "occupation": "software"})

# An arbitrary query against the database
scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

from selenium import webdriver
import scraperwiki
from time import sleep

# Read in a page
html = scraperwiki.scrape("http://foo.com")

# Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")

driver = webdriver.PhantomJS()
driver.get('https://www.reddit.com/')
sleep(10)
print 'fooobar'
title = driver.title

scraperwiki.sqlite.save(unique_keys=['name'], data={"name": title, "occupation": "software"})

# An arbitrary query against the database
scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

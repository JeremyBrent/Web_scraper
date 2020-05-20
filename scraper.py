from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd
import time

def init_browser():
    # Mac Users
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return(Browser('chrome', **executable_path, headless=False))
    
    # Windows Users
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    
    mars_dict = {}
    
    browser = init_browser()
    
    ## Nasa Mars News 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'html.parser')
    
    news_title = soup.find('ul',class_='item_list').find('div',class_='content_title').text
    mars_dict["news_title"] = news_title
    
    news_paragraph = soup.find('ul',class_='item_list').find('div',class_='article_teaser_body').text
    mars_dict["news_paragraph"] = news_paragraph
    
    ## Nasa Mars Images
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_id('full_image')
    time.sleep(5)
    html = browser.html
    soup = bs(html,'html.parser')
    url = browser.url
    marsimgsrc = soup.find('div',id="fancybox-lock").find('img',class_='fancybox-image')["src"]
    fullurl = url + marsimgsrc
    mars_dict["Mars_image"] = fullurl
    
    ## Mars Twitter Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = bs(html,'html.parser')
    mars_weather = soup.find('div',class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').find('span').text
    mars_dict["weather"] = mars_weather
    ## Mars facts table
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ["Characteristics","Values"]
    df.Characteristics = df.replace({":":""},regex=True)
    html_table = df.to_html().replace("\n","")
    mars_dict["facts"] = html_table

    ## USGS Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = bs(html,'html.parser')
    items = soup.find_all('div', class_="item")
    hemis_urls = []

    for item in items:
        title = (item.find('h3').text).replace(' Enhanced', '')
        browser.click_link_by_partial_text(title)
        time.sleep(5)
        soup = bs(browser.html, 'html.parser')

        full = soup.find('a', text='Sample')
        img_url = full['href']

        hemis_urls.append({'title': title, 'img_url': img_url})
        browser.back()

    browser.quit()    

    mars_dict["hemispheres"] = hemis_urls

    return mars_dict
    
    
    
    
    
    
    
    
    
    
    

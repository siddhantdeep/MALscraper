# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:31:38 2021

@author: siddh
"""

from bs4 import BeautifulSoup
import requests
import re
from time import sleep
#import add_mal_data_to_excel
def mal_scrape(site):
   
    page = requests.get(site)
    
    soup = BeautifulSoup(page.content,'html.parser')
    if soup.title.string!='404 Not Found - MyAnimeList.net\n':
        manga_title=soup.find('span',class_='h1-title')
        title_name=str(manga_title.span.contents[0].string) if manga_title.span else 'N/A'
     #   alt_name=manga_title.span.span.get_text() if manga_title.span.span else 'N/A'
     #   manga_type=soup.find_all(href=re.compile('type='))[0].get_text()
        info_arr=[]
        info_arr.append(['Page_Title'])
        info_arr[0].append(title_name)
        info_arr.append(['URL'])
        info_arr[1].append(site)
        
        for i in soup.find('div',id='content').table.tr.td.div.find_all('div'):
            display_value=i.get_text()
            if display_value and len(display_value) and ':' in display_value:
                li=(display_value.replace('\n','')).split(':')
                info_arr.append([x.strip() for x in li])
                #print(li)
            
   
        return info_arr
    else:
        sleep(0.6)
        return False
    
#mal_scrape('https://myanimelist.net/manga/4/')    
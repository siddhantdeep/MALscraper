# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 01:28:30 2021

@author: siddh
"""
import MalScrape
import add_mal_data_to_excel
import pandas as pd
from time import sleep
import random
from os import path
import make_MAL_sheet
from IPython import get_ipython

#import decimal
def commit_to_excel(frame):
    
    frame.drop_duplicates(inplace=True)   
    frame.to_excel('MAL_Manga_DB.xlsx',sheet_name='Manga',index=False)

def main():
     if not path.exists('MAL_Manga_DB.xlsx'):
         make_MAL_sheet.create_new_excel()
        
     mal_template=pd.read_excel('MAL_Manga_DB.xlsx', sheet_name='Manga')
     
     #default_col={i : 'N/A' for i in list(mal_template.columns)}    
     
     site='https://myanimelist.net/manga/{0}/'
     count=0
     exception_counter=0
     for i in range(122224, 140000):
         try:
             count+=1
             scrape_data=MalScrape.mal_scrape(site.format(i))
             if scrape_data:
                sleep(2.2)
                formated_data=add_mal_data_to_excel.add_to_excel(scrape_data,mal_template)
                print(i,formated_data['Page_Title'])
                mal_template=mal_template.append(formated_data, ignore_index=True)
                if count>=125:
                    get_ipython().magic('clear')
                    commit_to_excel(mal_template)
                    count=0
                    print(exception_counter)
                    #sleep(random.randrange(70, 110)
                
         except:
             exception_counter+=1
             print('{0} {1} \n\nNo of Stalls: {2}'.format(i,formated_data,exception_counter))
             
             i=i-1
             sleep(random.randrange(70, 120))
             continue
     commit_to_excel(mal_template)


if __name__ == '__main__':
    main()

    
#print(path.exists('MAL_Manga_DB.xlsx'))  
#print(random.randrange(60, 120))
#sleep(4)
    
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 01:28:46 2021

@author: siddh
"""
import pandas as pd
import numpy as np
import genres_parsing

    
def add_to_excel(manga_info, mal_template):
    column_name={i : 'N/A' for i in list(mal_template.columns)}    
        
    for li in manga_info:
        if li[0]=='Page_Title':
            column_name['Page_Title']=li[1]
        elif li[0]=='English':
            column_name['English_Title']=li[1]
        elif li[0]=='Japanese':
            column_name['Other_Titles']=li[1]
        elif li[0]=='Type':
            column_name['Type']=li[1]
        elif li[0]=='Chapters':
            column_name['Chapters']=li[1]
        elif li[0]=='Status':
            column_name['Status']=li[1]
        elif li[0]=='Published':
            column_name['Published']=li[1]
        elif li[0]=='Genres':
            column_name['Genres']=genres_parsing.genre_parse(li[1])
        elif li[0]=='Authors':
            column_name['Authors']=li[1]
        elif li[0]=='Serialization':
            column_name['Serialization']=li[1]
        elif li[0]=='Score':
            column_name['Score']=li[1].split()[0][:-1]
        elif li[0]=='Ranked':
            column_name['Ranked']=li[1].split()[0][:-1]
        elif li[0]=='Popularity':
            column_name['Popularity']=li[1]
        elif li[0]=='URL':
            column_name['URL']=li[1]
            
    #mal_template=mal_template.append(column_name, ignore_index=True)
    return column_name
    #mal_template.to_excel('MAL_Manga_DB.xlsx',sheet_name='Manga',index=False)
    
#add_to_excel(info_arr)

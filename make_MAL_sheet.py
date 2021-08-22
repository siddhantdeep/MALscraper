# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 01:03:56 2021

@author: siddh
"""

import pandas as pd
import numpy as np

def create_new_excel():
    mal_template = pd.DataFrame(columns=['Page_Title','English_Title','Other_Titles','Type','Chapters','Status','Published','Genres','Authors','Serialization','Score','Ranked', 'Popularity', 'URL'])
    mal_template.to_excel('MAL_Manga_DB.xlsx',sheet_name='Manga',index=False)
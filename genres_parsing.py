# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:20:35 2021

@author: siddh
"""
import re

def genre_parse(data):
#temp_data='ActionAction, AdventureAdventure, ComedyComedy, EcchiEcchi, FantasyFantasy, MagicMagic, Martial ArtsMartial Arts, RomanceRomance, SchoolSchool, ShounenShounen, HaremHarem, SupernaturalSupernatural, Slice of LifeSlice of Life, Sci-FiSci-Fi'
    final_data=[]
    for li in data.split(','):
        if ' ' in li.strip():
            exp='^[A-Z][a-z ]*[A-Z][a-z]*'
            final_data.append(re.findall(exp, li.strip())[0])
        elif '-' in li.strip():        
            exp='^[A-Z][a-z-]*[A-Z][a-z]*'
            final_data.append(re.findall(exp, li.strip())[0])
        else:
            exp='^[A-Z][a-z]*'
            final_data.append(re.findall(exp, li.strip())[0])
    return ', '.join(final_data)
   
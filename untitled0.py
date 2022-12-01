#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:58:17 2022

@author: riddhi
"""

import os
base_path = r'/Users/riddhi/Documents/GitHub/final_project'
ghg_path = os.path.join(base_path,'ghg-emissions-by-sector.csv' )
import pandas as pd
import numpy as np
import pandas_datareader.data as web
from pandas_datareader import wb
countries_df = wb.get_countries()
countries_df.head()
countries_df1 = countries_df.drop(columns=['iso3c', 'iso2c','region', 'lendingType' , 'adminregion', 'capitalCity', 'latitude', 'longitude'])
countries_df1 = countries_df1.loc[countries_df1['incomeLevel'] != 'Aggregates']
sectoral_ghg_df = pd.read_csv(ghg_path)
ghg_2019 = sectoral_ghg_df.loc[sectoral_ghg_df['Year'] == 2019]
df2=ghg_2019.dropna(subset=['Code'])
ghg_2 = df2.loc[df2['Code'] != "OWID_WRL"]




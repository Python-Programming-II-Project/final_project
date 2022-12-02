# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:16:42 2022

@author: khadk
"""

import pandas as pd
import os

data_ghg = pd.read_csv('per-capita-ghg-emissions.csv').dropna()
data_gdp = pd.read_csv('gdp-per-capita-worldbank.csv').dropna()
data_gdp_ghg = data_ghg.merge(data_gdp, how='outer', on=["Entity", "Year", "Code"]).rename(columns={"Entity": "Country", "Total including LUCF (per capita)": "CO2 Emmissions per capita", "GDP per capita, PPP (constant 2017 international $)": "GDP per capita"})

data_gdp_ghg = data_gdp_ghg[data_gdp_ghg.Year <= 2019]
data_gdp_ghg = data_gdp_ghg.drop(data_gdp_ghg[data_gdp_ghg.Country == "Afghanistan"].index)
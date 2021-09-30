#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:27:03 2021

@author: bgabriel
"""

import requests
import pandas as pd
import time
from datetime import datetime, timedelta


sd = datetime(2021,7,1)
ed = datetime(2021,8,1)
d = sd
dates = []
while d < ed:
    if d.weekday() >= 5:
        d = d + timedelta(days=1)
        continue
    dates.append(d.strftime("%Y-%m-%d"))
    d = d + timedelta(days=1)
    
opath = '/path'
fxpairs = ['EURUSD','GBPUSD','USDJPY','USDCAD','AUDUSD']

root_loc = "https://api.polygon.io/v2/aggs/ticker/C:{}/range/1/minute/{}/{}?adjusted=false&sort=asc&limit=1440&apiKey="

for date in dates:
    for ticker in fxpairs:
        print(f"Getting {ticker} for {date}")
        try:
            req_str = root_loc.format(ticker, date, date)
            response = requests.get(req_str)
            data = response.json()
            df = pd.DataFrame(data["results"])
            fdate = date.replace("-","")
            df.to_csv(f"{opath}/{ticker}_{fdate}.csv", index=False)
        except Exception as e:
            print(f"Exception: {e}")
    time.sleep(61)

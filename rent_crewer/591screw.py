import requests
import pandas as pd
import numpy as np
import time
from pymongo import MongoClient
conn = MongoClient('localhost', 27017)
db = conn['rent_591']
collection = db.rent

def get_data(firstRow,regionid):
    url = 'https://m.591.com.tw/mobile-list.html'
    #regionid: 台北市:1 新北市：3
    url_params = {
        'type' : 'rent',
        'dropDown' : 1,
        'version' : 2017,
        'firstRow' : firstRow,
        'regionid' : regionid,
        'region_id' : regionid
        }

    data_get = requests.get(url, params = url_params ,headers={'User-Agent': 'Custom'})
    
    total_rows = data_get.json()['totalRows']
    data = data_get.json()['data']
    
    return total_rows,data




def get_detail(regionid):
    total_rows = get_data(0,regionid)[0]
    print('total_rows',total_rows)
    start_time = time.time()
    for page in range(0,total_rows,8):
        print('page',page)
        if page == 0:
            page = page+1
        while True:
            try:       
                data_df = pd.DataFrame(get_data(page,regionid)[1])
                break
            except:
                time.sleep(10)
        
        data_houseid = data_df['houseid']

        for houseid in data_houseid:
            if type(houseid) != float:
                item_url = 'https://m.591.com.tw/iphone-houseRecordNew.html'
                item_url_params = {
                    'id' : houseid  
                    }
                while True:
                    try:       
                        item_data_get = requests.get(item_url, params = item_url_params ,headers={'User-Agent': 'Custom'})
                        break
                    except:
                        time.sleep(10)
                        
                item_data = item_data_get.json()['data']
                item_updatetime = item_data_get.json()['update']
                item_data['houseid'] = houseid
                item_data['update_time'] = item_updatetime

                collection.update({'houseid' : houseid},item_data, upsert = True)
    end_time = time.time() - start_time
    print('end_time:',end_time)
# get_detail(1)
# get_detail(3)
# data=get_data(1,1)
# print(data)






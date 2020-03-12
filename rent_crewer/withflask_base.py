from pymongo import MongoClient
import csv, os 
import pandas as pd

'''
資料擷取 搜尋
'''
conn = MongoClient('localhost', 27017)
db = conn['rent_591']
collection = db.rent


#搜尋
def search_enumera_region(sex):
    OJID_ls=[]
    rows = collection.find()   
    for index, items in enumerate(rows):
            if items['sex'] == f'{sex}':
                a = str(input("繼續選地區嗎?Y/N"))
                if a == 'Y':
                    b = input('Y.台北/N.新北')
                    if b =='Y':
                        region ='台北市'
                        OJI_sex =items['region'] 
                        if OJI_sex ==region:
                            OJID=items['_id']
                            OJID_ls.append(OJID)
                            break
                    elif b=='N':
                        region ='台北市'
                        OJI_region = items['region'] 
                        if OJI_region ==region:
                            OJID=items['_id']
                            OJID_ls.append(OJID)
                            break
                else:
                    
                    OJID=items['_id']
                    OJID_ls.append(OJID)
                    break
    return OJID_ls

def search_enumera_reuslt(a):
     
     rows = collection.find()   
     for index, items in enumerate(rows):
         
         if items['_id'] == a:
               OJID_Man= items['linkman']
               
               OJID_role = items['identity']
               
               OJID_mobile = items['mobile']
               
               OJID_Buldtype = items['parking_shape']
               
               OJID_sex = items['sex']
               
               info_dict ={
                    'Renter':OJID_Man,
                    'Renter_ID':OJID_role,
                    'mobile':OJID_mobile,
                    'Building_Type':OJID_Buldtype,
                    'SEX':OJID_sex
                    }

def filter(region,regg):
     OJID_ls=[]
     rows = collection.find()   
     for index, items in enumerate(rows):
         if items[f'{region}'] == regg:
             OJID=items['_id']
             OJID_ls.append(OJID)
     return OJID_ls
print('歡迎來到搜尋系統')
print('1.地區搜尋')
print('2.性別搜尋')
print('3.電話搜尋')
print('4.姓名搜尋')
print('5.是否為屋主搜尋')
print('6.搜尋結束')
p = input('請輸入搜尋物件')




        
    
    
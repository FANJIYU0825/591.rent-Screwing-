from pymongo import MongoClient
import csv, os 
import pandas as pd
import json

'''
租屋物件資料擷取
'''
conn = MongoClient('localhost', 27017)
db = conn['rent_591']
collection = db.rent



def search_enumera_region(region):
     OJID_ls=[]
     rows = collection.find()   
     for index, items in enumerate(rows):
         
#         for index, item in enumerate(items):
         if items['region'] == region:
             OJID=items['_id']
             OJID_ls.append(OJID)
     return OJID_ls

            
def search_enumera_reuslt(a):
     
     rows = collection.find()   
     for index, items in enumerate(rows):
         
#         for index, item in enumerate(items):
         if items['_id'] == a:
               OJID_Man= items['linkman']
               OJID_Man= f'Renter:{OJID_Man}'
               OJID_role = items['identity']
               OJID_role = f'Renter_ID:{OJID_role}'
               OJID_mobile = items['mobile']
               OJID_mobile = f'mobile:{OJID_mobile}'
               OJID_Buldtype = items['parking_shape']
               OJID_Buldtype = f'Building_Type:{OJID_Buldtype}'
               OJID_sex = items['sex']
               OJID_sex = f'SEX:{OJID_sex}'

     return OJID_Man,OJID_role,OJID_mobile,OJID_Buldtype,OJID_sex
             
             
def search_enumera_reuslt_df(a):
     
     rows = collection.find()   
     for index, items in enumerate(rows):
         
         if items['_id'] == a:
          #  角色
               OJID_Man= items['linkman']
               
          #身分
               OJID_role = items['identity']
          #電話 
               OJID_mobile = items['mobile']
               if OJID_mobile=='':
                    OJID_mobile=items['telephone']
                    if OJID_mobile=='':
                         OJID_mobile = 0
               else: pass
          #房屋種類     
               OJID_Buldtype = items['parking_shape']
          #性別
               OJID_sex = items['sex']
              
               info_dict ={
                    
                    'Renter':[OJID_Man],
                    'Renter_ID':[OJID_role],
                    'mobile':[OJID_mobile],
                    'Building_Type':[OJID_Buldtype],
                    'SEX':[OJID_sex]
                    }
                    
               
               select_df = pd.DataFrame(info_dict)
     return select_df          
     
def search_enumera_reuslt_json(a):
     
     rows = collection.find()   
     for index, items in enumerate(rows):
         
         if items['_id'] == a:
          #  角色
               OJID_Man= items['linkman']
               
          #身分
               OJID_role = items['identity']
          #電話 
               OJID_mobile = items['mobile']
               if OJID_mobile=='':
                    OJID_mobile=items['telephone']
                    if OJID_mobile=='':
                         OJID_mobile = 0
               else: pass
          #房屋種類     
               OJID_Buldtype = items['parking_shape']
          #性別
               OJID_sex = items['sex']
              
               info_dict ={
                    
                    'Renter':[OJID_Man],
                    'Renter_ID':[OJID_role],
                    'mobile':[OJID_mobile],
                    'Building_Type':[OJID_Buldtype],
                    'SEX':[OJID_sex]
                    }
                    
               [info_dict]
               
     return [info_dict]         
     

#【男生可承租】且【位於新北】的租屋物
def search_enumera_region2(region):
     OJID_ls=[]
     rows = collection.find()   
     for index, items in enumerate(rows):
         if items['sex'] != region:
               if items['region']=='新北市':
                    OJID=items['_id']
                    OJID_ls.append(OJID)         
     return OJID_ls



print('搜尋開始')
a = 1
with open ('file_males.json','a+') as j_file:
     res_males = search_enumera_region2('女生')
     for re_males in res_males:
          r_males =search_enumera_reuslt_json(re_males)
     # r_males.to_csv('filte_males.csv',index=False ,mode='a+')

          json_string = json.dumps(r_males,ensure_ascii=False)
          print(json_string)
          print(json_string, file=j_file,ens)
     
          
          print(a)
          a+=1
     
               
                  
          
     

  
#【臺北】【屋主為女性】【姓氏為吳】
# def search_enumera_region2(region):
#      OJID_ls=[]
#      rows = collection.find()   
#      for index, items in enumerate(rows):
#          if items['region'] == region:
#               if items['linkman']=='吳小姐':
#                     OJID=items['_id']
#                     OJID_ls.append(OJID)
#      return OJID_ls 
# print('搜尋開始')
# bic = 1         
# re_List = [f'{bic}']       
# res_wu = search_enumera_region2('台北市')
# for re_wu in res_wu:
#      r_wu =search_enumera_reuslt2(re_wu)
#      r_wu.to_csv('filte_wu.csv',index=False,mode='a+')
#      print(bic)
#      bic+=1

# 所有【非屋主自行刊登】的租屋物件
def search_enumera_region_NO(role):
     OJID_ls=[]
     rows = collection.find()   
     for index, items in enumerate(rows):
         if items['OJID_role'] != role:
                OJID=items['_id']
                OJID_ls.append(OJID)         
     return OJID_ls



print('搜尋開始')
a = 1
with open ('file_role.json','a+') as j_file:
     res_males = search_enumera_region2('屋主')
     for re_males in res_males:
        r_males =search_enumera_reuslt_json(re_males)
    # r_males.to_csv('filte_males.csv',index=False ,mode='a+')
        print(a)
        json_string = json.dumps(r_males,ensure_ascii=False)
        print(json_string)
        print(json_string, file=j_file)

        a+=1
from pymongo import MongoClient
import csv, os 
import pandas as pd
import json

'''
租屋物件資料擷取
'''
# 資料庫設定
conn = MongoClient('localhost', 27017)
db = conn['rent_591']
collection = db.rent
rows = collection.find()


def search_enumera_region_filter(region,regg):
     OJID_ls=[]
        
     for index, items in enumerate(rows):
         
         if items[f'{region}'] == regg:
             OJID=items['_id']
             OJID_ls.append(OJID)
     return OJID_ls

            
# def search_enumera_reuslt(a):
     
#      rows = collection.find()   
#      for index, items in enumerate(rows):
         

#          if items['_id'] == a:
#                OJID_Man= items['linkman']
#                OJID_Man= f'Renter:{OJID_Man}'
#                OJID_role = items['identity']
#                OJID_role = f'Renter_ID:{OJID_role}'
#                OJID_mobile = items['mobile']
#                OJID_mobile = f'mobile:{OJID_mobile}'
#                OJID_Buldtype = items['parking_shape']
#                OJID_Buldtype = f'Building_Type:{OJID_Buldtype}'
#                OJID_sex = items['sex']
#                OJID_kind = items['kind]

#      return OJID_Man,OJID_role,OJID_mobile,OJID_Buldtype,OJID_sex
             
# def search_enumera_reuslt_df(a):
     
#      rows = collection.find()   
#      for index, items in enumerate(rows):
         
#          if items['_id'] == a:
#           #  角色
#                OJID_Man= items['linkman']
               
#           #身分
#                OJID_role = items['identity']
#           #電話 
#                OJID_mobile = items['mobile']
#                if OJID_mobile=='':
#                     OJID_mobile=items['telephone']
#                     if OJID_mobile=='':
#                          OJID_mobile = 0
#                else: pass
#           #房屋種類     
#                OJID_Buldtype = items['parking_shape']
#           #性別
#                OJID_sex = items['sex']
#           #現況
#                OJID_kind = items['kind']    
#                info_dict ={
                    
#                     'Renter':[OJID_Man],
#                     'Renter_ID':[OJID_role],
#                     'mobile':[OJID_mobile],
#                     'Building_Type':[OJID_Buldtype],
#                     'SEX':[OJID_sex],
#                     'Kind': [OJID_kind]
#                     }
                    
               
#                select_df = pd.DataFrame(info_dict)
#      return select_df          
     
# def search_enumera_reuslt_json(a):
     
#      rows = collection.find()   
#      for index, items in enumerate(rows):
         
#          if items['_id'] == a:
#           #  角色
#                OJID_Man= items['linkman']
               
#           #身分
#                OJID_role = items['identity']
#           #電話 
#                OJID_mobile = items['mobile']
#                if OJID_mobile=='':
#                     OJID_mobile=items['telephone']
#                     if OJID_mobile=='':
#                          OJID_mobile = 0
#                else: pass
#           #房屋種類     
#                OJID_Buldtype = items['parking_shape']
#           #性別
#                OJID_sex = items['sex']
#       #現況
#                OJID_kind = items['kind']    
              
#                info_dict ={
               
#                'Renter':[OJID_Man],
#                'Renter_ID':[OJID_role],
#                'mobile':[OJID_mobile],
#                'Building_Type':[OJID_Buldtype],
#                'SEX':[OJID_sex],
#                'Kind':[OJID_kind]
               
#                }
#                [info_dict]
               
#      return [info_dict]         
     
''''
資料項目 
 info_dict ={
                    
                    'Renter':[OJID_Man],
                    'Renter_ID':[OJID_role],
                    'mobile':[OJID_mobile],
                    'Building_Type':[OJID_Buldtype],
                    'SEX':[OJID_sex]
                    'Kind''Kind':[OJID_ki:[OJID_kind]
                    nd]
                    }
''''

"""
----【男生可承租】且【位於新北】的租屋物----
"""

# def search_enumera_region2(sex,gender):
#      OJID_ls=[]
#      rows = collection.find()   
#      for index, items in enumerate(rows):
#          if items[f'{sex}'] != gender:
#                if items['region']=='新北市':
#                     OJID=items['_id']
#                     OJID_ls.append(OJID)         
#      return OJID_ls

# print('搜尋開始')
# a = 1
# with open ('file_males.json','a+',encoding='UTF-8') as j_file:
#      res_males = search_enumera_region2('sex','女生')
#      for re_males in res_males:
#           r_males =search_enumera_reuslt_json(re_males)
#      # r_males.to_csv('filte_males.csv',index=False ,mode='a+')

        #   json_string = json.dumps(r_males,ensure_ascii=False)
        #   print(json_string, file=j_file)
        #   print(json_string)
     
          
          # print(a)
          # a+=1
          # if a ==10:
          #        break
            
               
                  
          
     

"""
------【臺北】【屋主為女性】【姓氏為吳】----
"""

# def search_enumera_region2(region,role,linkman):
#      OJID_ls=[]
#      rows = collection.find()   
#      for index, items in enumerate(rows):
          
#           if items['region'] == region:
#                if items['OJID_role']==f'{role}':
#                     pass
#                else:
#                     return '限制屋主' 
#                if items[f'{linkman}']=='吳小姐':
                
#                     OJID=items['_id']
#                     OJID_ls.append(OJID)
#      return OJID_ls 
# print('搜尋開始')
# wu = 1         
# with open ('file_males.json','a+',encoding='UTF-8') as j_file:      
#      res_wu = search_enumera_region2('台北市','屋主','吳小姐')
#      for re_wu in res_wu:
#           r_wu = search_enumera_reuslt_json(re_wu)
#           json_string = json.dumps(r_wu,ensure_ascii=False)
#           print(json_string, file=j_file)
#           print(json_string)
     
          
#           print(wu)
#           wu+=1
#           if wu==10:
#                break
          
"""
-------所有【非屋主自行刊登】的租屋物件-----
"""

# def search_enumera_region_NO(role):
#      OJID_ls=[]
#      rows = collection.find()   
#      for index, items in enumerate(rows):
#          if items['identity'] != role:
#                 OJID=items['_id']
#                 OJID_ls.append(OJID)         
#      return OJID_ls

# print('搜尋開始')
# a = 1
# with open ('file_role.json','a+',encoding='UTF-8') as j_file:
#      res_roles = search_enumera_region_NO('屋主')
#      for re_role in res_roles:
#         r_role =search_enumera_reuslt_json(re_role)
#     # r_role.to_csv('filte_role.csv',index=False ,mode='a+') #csv檔案
#         print(a)
#         json_string = json.dumps(r_role,ensure_ascii=False)
        
#         print(json_string, file=j_file)
#         print(a,json_string)

#         a+=1


# # 以【聯絡電話】查詢租屋物件 
# def search_enumera_region_NO(phone):
#     OJID_ls=[]
#     rows = collection.find()   
#     for index, items in enumerate(rows):
#         if items['mobile'] != phone:
#             OJID=items['_id']
#             OJID_ls.append(OJID)         
#     return OJID_ls

# print('搜尋開始')
# phone = 1
# with open ('file_phone.json','a+',encoding='UTF-8') as j_file:
#     number = input('請輸入電話')
#     res_roles = search_enumera_regionNO(f'{number}')
#     for re_role in res_roles:
#         r_role =search_enumera_reuslt_json(re_role)
#     # r_males.to_csv('filte_males.csv',index=False ,mode='a+')
#         
#         json_string = json.dumps(r_role,ensure_ascii=False)
#         
#         print(json_string, file=j_file)
          # print(phone,json_string)
#         phone+=1
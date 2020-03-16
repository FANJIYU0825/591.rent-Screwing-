def search_use_menu():
    print('歡迎來到搜尋系統')
    print('1.地區搜尋')
    print('2.性別搜尋')
    print('3.電話搜尋')
    print('4.姓名搜尋')
    print('5.是否為屋主搜尋')
    print('6.搜尋結束')
    p = int(input('請輸入搜尋物件'))
    return p
            
def search_use_region(menu):
  menu=1
  if menu == True:
    print('台北按 1')
    print('新北按 2')
    K =int(input(''))
    if K==1:

        return 'region','台北市'
    elif K==2:
        return 'region','新北市'

menu = search_use_menu()
menu = int(menu)
region=search_use_region(menu)
print(region[1])
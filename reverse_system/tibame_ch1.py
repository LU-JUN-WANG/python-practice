from reverse_system import *
import re


while True:
    dname = input("請輸入名字: ")
    ddate = int(input("請輸入預約日期:"))

    while True:
        try:
            dphone = input("請輸入手機號碼: ")
            if not re.match(r'\(?^09[)-]?\d{8}', dphone):
                raise Exception('手機並非有效格式，請重新輸入')
        except Exception as err_msg:
            print(str(err_msg))
            continue
        else:
            break
    print("您的預約資料姓名為{}，手機號碼為{}，日期為{}".format(dname, dphone, ddate))
    confirm = input('資料是否正確[是/否]: ')
    store = input('要預約的門市為[Steven(1)/John(2)]:')
    if store == '1':
        if confirm == '是':
            data = RofSteven(dname, dphone, ddate)
            data.reverse_steven()
            again = input('是否繼續預定[是/否]: ')
            if again == '是':
                continue
            else:
                print('感謝您的預定')
                break
        else:
            continue
    elif store == "2":
        if confirm == '是':
            data = RofJohn(dname, dphone, ddate)
            data.reverse_john()
            again = input('是否繼續預定[是/否]: ')
            if again == '是':
                continue
            else:
                print('感謝您的預定')
                break
        else:
            continue

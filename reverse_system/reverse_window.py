import tkinter as tk
from tkinter import messagebox
from reverse_system import *
import re
def steven(n,p,d):
    data = RofSteven(n,p,d)
    data.reverse_steven()
def john(n,p,d):
    data = RofJohn(n,p,d)
    data.reverse_john()




window = tk.Tk()
window.title('歡迎來到預約系統')
window.geometry('800x603')
canvas = tk.Canvas(window,height=280,width=603)
img_file = tk.PhotoImage(file='unknown.png')
image = canvas.create_image(0,0,anchor='nw',image=img_file)
canvas.pack(side='top')
tk.Label(window,text='預訂者名字:').place(x=150,y=300)
tk.Label(window,text='預訂者手機:').place(x=150,y=350)
tk.Label(window,text='預訂日期:').place(x=150,y=400)
choose = tk.StringVar()
c1 = tk.Radiobutton(window, text='Steven門市', variable=choose, value='Steven門市')
c1.place(x=180,y=450)
c1.select()
c2 = tk.Radiobutton(window, text='John門市', variable=choose, value='John門市')
c2.place(x=300,y=450)
uname = tk.StringVar()
iname = tk.Entry(window,textvariable=uname)
iname.place(x=260,y=300)
uphone = tk.StringVar()
uphone.set('09xxxxxxxx')
iphone= tk.Entry(window,textvariable=uphone)
iphone.place(x=260,y=350)
udate = tk.StringVar()
idate = tk.Entry(window,textvariable=udate)
idate.place(x=260,y=400)
def reverse_in():
    try:
        if not re.match(r'\(?^09[)-]?\d{8}', uphone.get()) or len(uphone.get())!=10:
            raise Exception()
    except:
        tk.messagebox.showerror(title="錯誤", message='手機格式輸入錯誤，請重新輸入')
    else:
        askbox = tk.messagebox.askquestion(title='預訂者基本資料',message="您的預約資料姓名為{}，手機號碼為{}，日期為{}，預定門市為{}".format(uname.get(), uphone.get(), udate.get(),choose.get()))
        if askbox == 'yes' and choose.get() == "Steven門市":
            steven(uname.get(), uphone.get(), udate.get())
            tk.messagebox.showinfo(message='感謝您的預定')
        elif askbox == 'yes' and choose.get() == "John門市":
            john(uname.get(), uphone.get(), udate.get())
            tk.messagebox.showinfo(message='感謝您的預定')
        elif askbox == 'no':
            tk.messagebox.showerror(title='錯誤', message="資料輸入錯誤，請重新輸入")
def quit():
    qb=tk.messagebox.askquestion(title='離開', message='是否離開預約系統')
    if qb == 'yes':
        window.destroy()
bt_reverse = tk.Button(window,text = 'reverse',command=reverse_in)
bt_reverse.place(x=260,y=500)
qu_reverse = tk.Button(window,text = 'quit',command=quit)
qu_reverse.place(x=350,y=500)
window.mainloop()

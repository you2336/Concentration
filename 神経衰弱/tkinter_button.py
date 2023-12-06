import tkinter as tk

def f0():
  print('f0',end='')

def f1():
  print('f1',end='')
  
def f2():
  print('f2',end='')
  
def f3():
  print('f3',end='')

def f4():
  print('f4',end='')


fream = tk.Tk()
fream.geometry('400x400')
fream.title('神経衰弱')

#ボタン作成
bot1 = tk.Button(fream,text='A1',command=f1)
bot1.place(x= 10,y=10)
bot2 = tk.Button(fream,text='B2',command=f2)
bot2.place(x= 60,y=10)
bot3 = tk.Button(fream,text='C3',command=f3)
bot3.place(x=110,y=10)
bot4 = tk.Button(fream,text='D4',command=f4)
bot4.place(x=160,y=10)

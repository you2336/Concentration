import tkinter as tk
from tkinter import ttk
import threading
import random
import time
import datetime
date = datetime.datetime.now()
date = str(date.month)+'/'+str(date)[8:-7]

debug=True
pointer = ["target","question_arrow"]
tramps  = ['']   *52#シャッフルしたトランプ
Turn    = []        #裏返したトランプ
img     = ['']   *53#昇順トランプ
button  = ['']   *52#ボタン
count=0
turn_count=0
tmc='00:00'
tm=0
#シャッフルしたトランプを用意       
for i in range(52):
    while True:
        pull=random.randint(0,51)
        if not(pull in tramps):
            tramps[i]=pull
            break
#プレイ時間取得
def tmc1():
    global tmc, count, tm
    while True:
        if len(Turn):
            tm=time.time()
            while True:
                tmc=int(time.time()-tm)
                tmc2="経過時間 "+str(tmc//60).rjust(2,'0')+":"+str(tmc%60).rjust(2,'0')
                timer.configure(text=tmc2)
                time.sleep(1)
            print(tmc2)
#ボタンを押されたときの処理関数
def callback(i):
  def x():
    global frame, tramps, Turn, img, button, count, clear_window, turn_count, tmc, tm
    turn_count += 1
    Turn.append(i)
    counter.configure(text="めくった回数："+str(turn_count).rjust(3))
    if len(Turn)+count >= 53:#53
        tmc=int(time.time()-tm)
        tmc3="経過時間 "+str(tmc//60).rjust(2,'0')+":"+str(tmc%60).rjust(2,'0')
        timer.configure(text=tmc3)
        #button[Turn[0]].lower();button[i].lower()
        for o in range(52):
            button[o].lower()
        d()
        log=date+'|'+str(turn_count).rjust(20)+'|'+str(tmc//60).rjust(2,'0')+":"+str(tmc%60).rjust(2,'0')+'\n'
        print(log)

        st = open("logs.txt","a")
        st.close()
        log_count=0
        st = open("logs.txt",'r')
        log_txt = st.read()
        st.close()
        if not log_txt:
            st = open("logs.txt","a")
            st.write("<No>        <日時>       ＜めくった回数＞＜タイム＞\n")
            st.close()
            st = open("logs.txt",'r')
            log_txt = st.read()
            st.close()
        for p in log_txt:
            if p == '\n':
                print("777")
                log_count+=1

        st = open("logs.txt","a")
        st.write(str(log_count).rjust(8)+'|'+log)
        st.close()
        st = open("logs.txt")
        print(st.read())
        st.close()
        
        clear_window.tkraise()
    if len(Turn) == 2 and (tramps[Turn[0]] % 13) == (tramps[Turn[1]] % 13):
        count+=2
        pair_counter.configure(text="そろったペア："+str(count//2).rjust(3))
    if len(Turn)>2:
        if (tramps[Turn[0]] % 13) == (tramps[Turn[1]] % 13):
            button[Turn[0]].lower();button[Turn[1]].lower()
        else:
            button[Turn[0]].configure(image=img[52],state=tk.NORMAL)
            button[Turn[1]].configure(image=img[52],state=tk.NORMAL)
        Turn=Turn[2:]
    button[i].configure(image=img[i],state=tk.DISABLED)
    d()
  return x

def d():
    for i in range(52):
        print(str(tramps[i]%13+1).rjust(2),end='  ')
        if not((i+1)%13):
            print()
    print()
# G A M E _ S T A R T
d()
root = tk.Tk()
root.geometry('1212x550')#X=(余白、一枚目の座標)+xlen*12(12枚目までの余白とカードの幅)+(13枚目の幅)+(始めと同じ幅の余白)
root.title('神経衰弱')   #Y=(余白、一枚目の座標)+ylen* 3( 3段目までの余白とカードの幅)+( 4枚目の幅)+(  　任意    の余白)
root.resizable(width=0, height=0)#tramp_size =  1~ 9:(136,200)
                                 #             10~13:(204,300)
                                 #                  :(273,400)
clear_window = tk.Frame(root,width=1350,height=550,bg='#416061',cursor=pointer[0])
clear_window.place(x=300,y=240)
Title = tk.Label(clear_window, text="C　L　E　A　R　！", font=("MSゴシック", "50", "bold"))
Title.pack()
frame = tk.Frame(root,width=1350,height=550,bg='#416061',cursor=pointer[0])
frame.place(x=0,y=0)
timer = ttk.Label(frame,text="経過時間"+tmc,background='#416061',foreground='#ffffff',font=("MSゴシック", "20", "bold"))
timer.place(x=950,y=10)
counter = ttk.Label(frame,text="めくった回数："+str(turn_count).rjust(3),background='#416061',foreground='#ffffff',font=("MSゴシック", "10", "bold"))
counter.place(x=50,y=10)
pair_counter = ttk.Label(frame,text="そろったペア："+str(count//2).rjust(3),background='#416061',foreground='#ffffff',font=("MSゴシック", "10", "bold"))
pair_counter.place(x=50,y=30)

#ボタンを作成 & 設置
ylen=120;xlen=90
for i in range(52):
  if tramps[i]%13 < 10:#画像サイズ調整
    img[i] = (tk.PhotoImage(file="tramp ("+str(tramps[i])+").png").subsample(2, 2))
  else:
    img[i] = (tk.PhotoImage(file="tramp ("+str(tramps[i])+").png").subsample(3, 3))
  button[i]=(tk.Button(root,image=img[i],command=callback(i),cursor=pointer[1]))
  button[i].place (x=(xlen *(i%13)) +32,y=(ylen * (i//13)) +55)
img[52] = (tk.PhotoImage(file="tramp (52).png").subsample(4, 4))

for i in range(52):
    button[i].configure(image=img[52])
    
thread = threading.Thread(target=tmc1, daemon=True)
thread.start()
root.mainloop()

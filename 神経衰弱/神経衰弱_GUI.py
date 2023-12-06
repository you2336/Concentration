import tkinter as tk
import random
import time
debug=True
pointer = ["target","question_arrow"]
tramps  = ['']   *52#シャッフルしたトランプ
Turn    = []        #裏返したトランプ
img     = ['']   *53#昇順トランプ
button  = ['']   *52#ボタン
count=0

#シャッフルしたトランプを用意       
for i in range(52):
    while True:
        pull=random.randint(0,51)
        if not(pull in tramps):
            tramps[i]=pull
            break


#ボタンを押されたときの処理関数
def callback(i):
  def x():
    global frame, tramps, Turn, img, button, count, clear_window
    Turn.append(i)
    if len(Turn)+count >= 52:
        button[Turn[0]].lower();button[i].lower()
        d()
        clear_window.tkraise()
    if len(Turn)>2:
        if (tramps[Turn[0]] % 13) == (tramps[Turn[1]] % 13):
            button[Turn[0]].lower();button[Turn[1]].lower()
            count+=2
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
root.geometry('1212x510')#X=(余白、一枚目の座標)+xlen*12(12枚目までの余白とカードの幅)+(13枚目の幅)+(始めと同じ幅の余白)
root.title('神経衰弱')   #Y=(余白、一枚目の座標)+ylen* 3( 3段目までの余白とカードの幅)+( 4枚目の幅)+(  　任意    の余白)
root.resizable(width=0, height=0)#tramp_size =  1~ 9:(136,200)
                                 #             10~13:(204,300)
                                 #                  :(273,400)
clear_window = tk.Frame(root,width=1350,height=550,bg='#416061',cursor=pointer[0])
clear_window.place(x=470,y=240)
Title = tk.Label(clear_window, text="C　L　E　A　R　！", font=("MSゴシック", "20", "bold"))
Title.pack()
frame = tk.Frame(root,width=1350,height=550,bg='#416061',cursor=pointer[0])
frame.place(x=0,y=0)

#ボタンを作成 & 設置
ylen=120;xlen=90
for i in range(52):
  if tramps[i]%13 < 10:#画像サイズ調整
    img[i] = (tk.PhotoImage(file="tramp ("+str(tramps[i])+").png").subsample(2, 2))
  else:
    img[i] = (tk.PhotoImage(file="tramp ("+str(tramps[i])+").png").subsample(3, 3))
  button[i]=(tk.Button(root,image=img[i],command=callback(i),cursor=pointer[1]))
  button[i].place (x=(xlen *(i%13)) +32,y=(ylen * (i//13)) +25)
img[52] = (tk.PhotoImage(file="tramp (52).png").subsample(4, 4))

for i in range(52):
    button[i].configure(image=img[52])

root.mainloop()

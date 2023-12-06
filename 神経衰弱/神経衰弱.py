import random
import os

sort_tramp=[]
rand_tramp=[]
judge=[]
index_list=[]
flag=[0]*52

#トランプ52枚を用意
for i in range(0,52,1):
    sort_tramp.append(i)
def display_one(x):
    x2=x//13
    if   x2 == 0:
        print("♡"+" "+str((x%13)+1).rjust(2),end="")
    elif x2 == 1:
        print("♤"+" "+str((x%13)+1).rjust(2),end="")
    elif x2 == 2:
        print("♦"+" "+str((x%13)+1).rjust(2),end="")
    elif x2 == 3:
        print("♧"+" "+str((x%13)+1).rjust(2),end="")
    else:
        print("error",end='')
    
def display_all(x):
    if (x==0)or(x==2):
        k=-1
        print("    [0]      [1]    [2]     [3]")
        for i in range(13):
            print("["+str(i).rjust(2)+"]",end="")
            for j in range(4):
                k+=1
                if   flag[k] == 0:
                    print("■■",end="")
                elif flag[k] == 1:
                    display_one(rand_tramp[k])
                elif flag[k] == -1:
                    print("□□",end="")
                else:
                    print("××",end="")
                print("    ",end="")
            print()
    if (x==1)or(x==2):
        for i in range(52):
            if (i % 4 ) == 0:
                print()
            print(str(i).rjust(2),":",str(rand_tramp[i]).rjust(2),"=",str(flag[i]).rjust(2),end="  ")
    print("\n",judge)
    print("",index_list)
def all_clear():
    count=0
    for i in range(52):
        if flag[i] == -1:
            count+=1
            if count == 52:
                print("おめでとうございます。クリアです")
        else:
            break
#ランダムに入れなおす
while True:
    pull = random.randint(0,51)
    if (type(sort_tramp[pull]) == int):
        rand_tramp.append(sort_tramp[pull])
        sort_tramp[pull]=False
        """print(sort_tramp[pull],rand_tramp[-1],len(rand_tramp))
        print(rand_tramp)
        print(sort_tramp)"""
        if len(rand_tramp) == 52:
            break

#  G A M E _ S T A R T
display_all(2)
while True:#1ターン
    while True:#2枚トランプを選ぶループ
        print("\n",len(judge)+1,"枚目")
        #トランプを選択
        select_y=input("縦を選択")
        select_x=input("横を選択")
        try:
            select_y=int(select_y)
            select_x=int(select_x)
        except ValueError:
            print("対応していない文字の入力がありました")
            continue
        if ((select_y < 0 or 12 < select_y) or (select_x<0 or 3 < select_x)):
            print("範囲外の入力です")
            continue
        index=select_y*4 + select_x
        if flag[index] == -1:
            print("既にclearしたトランプです")
            continue
        #トランプの選択を終了_
        flag[index]=1
        judge.append(rand_tramp[index])
        index_list.append(index)
        display_all(0)
        if len(judge) == 2:
            if judge[0] == judge[1]:
                judge.pop(-1)
                index_list.pop(-1)
                print("同じカードが選択されましたので選びなおして")
                continue
            break
        else:
            continue
    print("めくったカードは")
    display_one(judge[0])
    print("                ")
    display_one(judge[1])
    print("です！")
    #ここで「judge」に二つトランプが入っている
    if (judge[0] % 13) == (judge[1] % 13):
        flag[index_list[0]]=flag[index_list[1]]=-1
        print("数字が一致しました")
    else:
        flag[index_list[0]]=flag[index_list[1]]=0
        print("数字が一致しませんでした")
        
    index_list=[]
    judge=[]
    display_all(1)

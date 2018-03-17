#https://open.kattis.com/problems/falsesecurity
#PYTHON

from __future__ import print_function
import sys


morse =['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','..--','---.','.-.-','----']
leng=[]
msg=[]
ch=''
count=0
c='start'
c2=1

c=raw_input()
while True:
    leng=[]
    msg=[]
    ch=''
    count=0
    for i in c:
        a=ord(i)
        if(a==95):                  #correcting for the symbols
            a=91
        elif(a==46):
            a=92
        elif(a==44):
            a=93
        elif(a==63):
        leng.append(len(morse[a-65]))         #calculating lengths

    leng.reverse()

    for j in leng:
        i=0
        ch=''
        for i in range(j):
            ch+=msg[count]              #accessing letters from the extracted msg
            count+=1

        a=(morse.index(ch))
        if(a==26):                  #correcting for the symbols
            a=30
        elif(a==27):
            a=-19
        elif(a==28):
            a=-21
        elif(a==29):
            a=-2

        print(chr(a+65), end='')

    print()
    c=''

    try:
        c = raw_input()
        if(c==''):
            break

    except EOFError:
        sys.exit();

    c2+=1

#https://open.kattis.com/problems/falsesecurity
#PYTHON

from __future__ import print_function
import sys

#print("test")
morse =['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','..--','---.','.-.-','----']
#alpha = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z];
#print(len(morse))

#print(ord(c[0]))
leng=[]
msg=[]
ch=''
count=0
c='ABC'
c='DSU.XFNCJEVE.OE_UJDXNO_YHU?VIDWDHPDJIKXZT?E'
c='ADAWEKHZN,OTEATWRZMZN_IDWCZGTEPION'
c='QEWOISE.EIVCAEFNRXTBELYTGD.'
#c='?EJHUT.TSMYGW?EJHOT'

c='start'

c2=1
#print()
c=raw_input()
while True:


    leng=[]
    msg=[]
    ch=''
    count=0
    for i in c:
        a=ord(i)
        #print(a)
        if(a==95):                  #correcting for the symbols
            a=91
        elif(a==46):
            a=92
        elif(a==44):
            a=93
        elif(a==63):
            a=94
        #print(a)
        #(morse[a-65])
        msg+=(morse[a-65])              #converting to ascii
        #print(len(morse[a-65]))
        leng.append(len(morse[a-65]))         #calculating lengths
        #print('d')
    leng.reverse()
    #print(leng)
    #print(msg)
    for j in leng:
        i=0
        ch=''
        for i in range(j):
            ch+=msg[count]              #accessing letters from the extracted msg
            count+=1

        #print(ch)
        #print(morse.index(ch))
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
        #print(c)

    except EOFError:
        #print(EOFError)
        sys.exit();
    #print(c2)
    c2+=1





#print("\n\n\n\n")

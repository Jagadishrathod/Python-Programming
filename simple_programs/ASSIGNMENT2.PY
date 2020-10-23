# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:34:25 2020

@author: RATHOD
"""

# def func(mx, i):
#     for ind in range(i, n-1):
#         print(mx[i][ind], end=' ')
#     for ind in range(i+1, n-i):
#         print(mx[ind][n-1-i], end=' ')
#     for ind in range(n-2-i, i, -1):
#         print(mx[n-1-i][ind], end=' ')
#     for ind in range(n-i-1,i, -1):
#         print(mx[ind][i], end=' ')
# n = 7    
# func(mx,2)

# import random
# import datetime
# birthday = []
# i=0
# while(i<50):
#     year=random.randint(1895,2020)
#     if (year%4==0 and year%100!=0 or year%400==0):
#         leap=1
#     else:
#         leap=0
#     month=random.randint(1,12)
#     if(month==2 and leap==1):
#         day=random.randint(1,29)
#     elif(month==2 and leap==0):
#         day=random.randint(1,28)
#     elif(month==7 or month==8):
#         day=random.randint(1,31)
#     elif(month%2!=0 and month<7):
#         day=random.randint(1,31)
#     elif(month%2==0 and month>7 and month<12):
#         day=random.randint(1,31)
#     else:
#         day=random.randint(1,30)
#     dd=datetime.date(year,month, day)
#     day_of_year=dd.timetuple().tm_yday
#     i = i+1
#     birthday.append(day_of_year)
    
# birthday.sort()
# i=0
# while(i<50):
#     print(birthday[i])
#     i=i+1
import random
name = ["apple","baba blak","crown","devil"]

def create_question(name):
    n=len(name)
    letters=list(name)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter, name):
    c=name.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,name,letter):
    ref=list(name)
    qu_list=list(qn)
    temp=[]
    n=len(name)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def play():
    p1 = input("palyer1! please enter your name: ")
    p2 = input("palyer2! please enter your name: ")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1,"your turn: ")
            picked_name=random.choice(name)
            qn=create_question(picked_name)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("you letter: ")
                if(is_present(letter,picked_name)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_name,letter)
                    print(modified_qn)
                    d=input('press 1 to guess name or 2 to unclock another letter: ')
                    if d==1:
                        ans=input('your answer:')
                        if ans==picked_name:
                            pp1=pp1=1
                            print("correct")
                            not_said= False
                            print(p1, "your score: ", pp1)
                        else:
                            print("wrong answer. try again")
                    else:
                        print(letter, "not found")
                c=int(input("press 1 to continue or 0 to quit"))
                if c==0:
                    print(p1, "your score: ",pp1)
                    print(p2, "your score: ",pp2)
                    print("thanks for playing")
                    willing=False
                
        else:
            print(p1,"your turn: ")
            picked_name=random.choice(name)
            qn=create_question(picked_name)
            print(qn)
            modified_qn=qn
            not_said=True            
            while not_said:
                letter=input("you letter: ")
                if(is_present(letter,picked_name)):
                    modified_qn=unlock(modified_qn,picked_name,letter)
                    print(modified_qn)
                    d=input('press 1 to guess name or 2 to unclock another letter')
                    if d==1:
                        ans=input('your answer:')
                        if ans==picked_name:
                            pp1=pp1=1
                            print("correct")
                            not_said= False
                            print(p1, "your score: ", pp1)
                        else:
                            print("wrong answer. try again")
                    else:
                        print(letter, "not found")
                c=int(input("press 1 to continue or 0 to quit"))
                if c==0:
                    print(p1, "your score: ",pp1)
                    print(p2, "your score: ",pp2)
                    print("thanks for playing")
                    willing=False
            turn=turn+1
play()
                        
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:05:48 2024

@author: sdishakamleshkuma
"""
#Designed a word jumble game

import random

L=["Apple","Laptop","Computer","Mobile","Hyundai","mercedes","samsung"]
random.shuffle(L)

points=0

for word in L:
    
    #jumble word
    
    temp=list(word)
    random.shuffle(temp)
    jword=''.join(temp)
    
    attempt=0
        
    while attempt<3:
        #show the word to user
        
        print(jword.upper())
        print("\nYour input:")
        
        #ask user for input
        
        uword=input("->")
        
        hint=[]
        for i in range (len(L)):
            if uword[i]==L[i]:
        
        #compare the user input with OG word
        #update points
        
        if(uword.lower()==word.lower()):
            points+=1
            print("Correct")
        else:
            print("Incorrect")
        
#print result

if(points>6):
    print("Excellent")
elif(3<= points <=6):
    print("Good")
else:
    print("Ugly")
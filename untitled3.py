# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:28:09 2024

@author: sdishakamleshkuma
"""

import random

L=[("Apple","Fruit"),("Laptop", "portable electronic device"),("Computer","gaming device"),("Mobile","calling device"),("Hyundai","Car"),("mercedes","lux. car"),("samsung","brand")]
random.choice(L)

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
        
        #compare the user input with OG word
        #update points
        
        if(uword==word):
            points+=1
            print("Correct")
        else:
            if(attempt<3):
                attempt+=1
                print("Incorrect")
                print(f"Hint:{L}")
            else:
                print("Incorrect")
            
if(points>6):
    print("Excellent")
elif(3<= points <=6):
    print("Good")
else:
    print("Ugly")       

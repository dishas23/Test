# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:29:37 2024

@author: sdishakamleshkuma
"""

# Program to tell if the result was positive, negative or zero
# after subtraction of two numbers

# input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


# process
res = a - b

# output
print("-"*50)    #print line "-" * 50 times
print("DIFFERENCE  : ", abs(a - b))    

# ---------- print results here with if..else.. block

if (res>0):
    print("The result is positive")
    
    if(res>70):
        print("Good")
    elif(res>=30 and res<=70):
        print("Bad")
    else:
        print("Ugly")
        
elif (res<0):
    print("result is negative")
else:
    print("Result is zero")
print("-"*50)

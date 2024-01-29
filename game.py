# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:38:49 2024

@author: sdishakamleshkuma
"""

import random

def wordhint():
    word_hint=[("Apple","Fruit"),("Laptop", "portable electronic device"),("Computer","gaming device"),("Mobile","calling device"),("Hyundai","Car"),("mercedes","lux. car"),("samsung","brand")]
    return random.choice(word_hint)

def jumble_word(word):
    jumbled_word=list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)
def hints(hint):
    print(f"Hint: {hint}")
    
chosen_word , hint = wordhint()
jumbled_word=jumble_word(chosen_word)

print(jumbled_word)

attempts=3
while attempts>0:
    user_word=input("Input guess").lower()
    if user_word==chosen_word:
        print("Correct")
        break
    else:
        attempts-=1
        if attempts>0:
            hints(hint)
        else:
            print("Sorry, out of attempt")
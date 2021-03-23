# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:35:33 2021

@author: micha
"""

def revword(word:str) -> str:
    index=len(word)
    letter=""
    for i in range(index):
        letter=letter+word[index-1]
        index=index-1
    # print(letter.lower())  
    return letter.lower()
    


def countword()-> int:
  # file=input("enter file")
    count=1
    fhand=open('text.txt')
    word=fhand.readline()
    for line in fhand:   #זה רץ על שורות
        WordsInLine=line.split() 
        num=len(WordsInLine)
        for i in range(num):        #זה רץ על מילים
            val=line.split()
            value=revword(val[i])
            if(word.strip()==value.strip()):
                count=count+1
            # print(value)       
    return count
    

           

    # print(WordsInLine)
#a = input("enter word ")
#revword(a)

# print(countword())
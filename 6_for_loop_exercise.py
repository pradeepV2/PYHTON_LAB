# -*- coding: utf-8 -*-
"""6. For loop exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LX_AkmryxljFo0_btWBnY2vZFt2kcBnf

After flipping a coin 10 times you got this result

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

Using for loop figure out how many times you got heads
"""

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

j=0
k=0
for i in result:
  if i == "heads" :
    j= j+1
    print("HEADS :", j)
  else :
    k=k+1
    print("TAILS :", k)

#Print square of all numbers between 1 to 10 except even numbers

for i in range(1,11):
   print("print :", i)
   print("i square :" , i*i)


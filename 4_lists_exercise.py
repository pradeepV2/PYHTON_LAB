# -*- coding: utf-8 -*-
"""4. Lists exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VnO66ApkTK2zII5q3chpB2VjSux6zh8q

Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""

expenses =[2200, 2350, 2600, 2130,2190]
expenses

Month =["January", "February", "March", "April", "May"]
Month

1. In Feb, how many dollars you spent extra compare to January?

Jan_exp = 2200
Feb_exp = 2350
Mar_exp = 2600
Apr_exp = 2130
May_exp = 2190

Extra_spent_in_feb = Jan_exp - Feb_exp
Extra_spent_in_feb

expenses =[2200, 2350, 2600, 2130,2190]
expenses

feb_extra_exp = expenses[1] - expenses[0]
feb_extra_exp

# 2. Find out your total expense in first quarter (first three months) of the year.
first_quart = expenses[0] + expenses[1] + expenses[2]
first_quart

#3. Find out if you spent exactly 2000 dollars in any month
expenses

2000 in expenses

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses
expenses.append(2000)
expenses

# 5. You returned an item that you bought in a month of April and got a refund of 200$.
# Make a correction to your monthly expense list based on this
expenses[3]

expenses[3] - 200

exp_3 = expenses[3] - 200

expenses

expenses.insert(3,exp_3)
expenses


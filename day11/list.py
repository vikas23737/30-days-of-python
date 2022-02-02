#1st program print list in reverse order using while loop
import builtins
from pdb import lasti2lineno
from typing import List


l= [1,2,3,4,5,6]
i= len(l)-1 
while i>= 0:
    print(l[i],end=' ')
    i=i-1
#2nd program Concentrate two list index wise
ListA=['Com','con','fo']
ListB=['mon','verge','cus']
print("Given list A:",ListA)
print("Given list B:",ListB)
res=[i+j for i,j in zip(ListA,ListB)]
print("The Concentrate Lists:",res)
#3rd program take input in the list using loop
list=[]
n=int(input("Enter number of element:"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
#4 program  Display number from a list using loop
l=[1,2,3,4,5,6,7]
print("printing number without list:")
for i in range(len(l)):
    print(l[i], end=' ')
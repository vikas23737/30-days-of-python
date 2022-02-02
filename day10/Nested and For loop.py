#1st program for loop program to print multiplication
from sre_constants import RANGE


a=int(input("Enter the number upto you want table:"))
for i in range(1,a+1):
    for j in range(1,11):
        k=i*j
        print(k,end=" ")
    print()

#2nd program print ractangle pattern with 5 row and 3 coloum of star
Rows = 5
Coloumn= 3
for i in range(Rows):
    j=0
    while(j<Coloumn):
        print('*', end=" ")
        j=j+1
    i= i+1
    print(" ")
# 1st program for calculate compound interest
print("calculate compound interest")
p  = int(input("Enter the principle amount:"))
t = int(input("Enter the year:"))
r = float(input("Enter the rate of interest:"))
a =p*(pow((1+r/100),t))
print ("amount=",a)
ci = a-p
print("compount interest=",ci)

#2nd program for calculating percentage
print("calculate percentage")
a=float(input("enter your marks:"))
per=100
b=float(input("enter total marks:"))
c=a*per/b
print("your percentage:",c)

#3rd program for print first , middle and last value string 
s="vikas"
t="rathore"
print(s[0])
print(s[2])
print(t[-1])

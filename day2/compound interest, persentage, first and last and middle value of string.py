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
a=()
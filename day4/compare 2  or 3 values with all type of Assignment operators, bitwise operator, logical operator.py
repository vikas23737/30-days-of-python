#1st program compare 2 or 3 values with all type of assignment operators
m=int(input("Enter first value: "))
n=int(input("Enter second value:"))
print("Assign(+):",m+n)

o=int(input("Enter first value: "))
p=int(input("Enter second value: "))
o+=p
print(f"Add and Assign: o+=p:",o)

q=int(input("Enter first value :"))
r=int(input("Enter second value :"))
q-=r
print(f"Subtract and Assign q-=r:",q)

s=int(input("Enter first value :"))
t=int(input("Enter second value :"))
s*=t
print(f"Multiply and Assign s*=t ",s)

u=int(input("Enter first value "))
v=int(input("Enter second value "))
u/=v
print(f"Divide and Assign u/=v",u)
#2nd program compare 2or 3 value with all type of bitwise operator

a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
print("The value of a&b(Bitwise And) is :",a&b)
print("The value of a|b(Bitwise Or) is :",a|b)
print("The value of ~a(Bitwise Not) is :",~a)
print("The value of a^b(Bitwise Xor) is :",a^b)
#3rd program logical operator

a=True
b=False
print(f"{a} and {b} will be : {a and b}")
print(f" {a} or {b} will be : {a or b} ")
print(f"{a} not will be : { not a}")

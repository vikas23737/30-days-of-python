#1st program to display 100 number in reverse order
i=100
print("Numbers in reverse order")
while(i>=1):
    print(i,end=" ")
    i=i-1

#2nd program to display prime number within range
num =1
while(num<=100):
    count =0
    i =2
    while(i<=num//2):
        if (num%i== 0):
             count= count+1
             break
        i= i+1
    if(count==0 and num!=1):
       print("%d"%num,end=" ")
    num=num+1
#3rd program  sum of series upto n terms
n=int(input("Enter number upto which you want to add in series"))
i=1
sum=0

    
#1st program To check the number is divisible by 2 or not
num = int(input("Enter Number:"))
if num%2==0:
    print(num,"is divisible by 2")
else:
    print(num,"is not divisible by 2")

#2nd program make a grading system program according to the values given by user 
mark = int(input("Enter your Marks:"))
if( mark<=100 and mark>=80):
    print("Excellent Result! You have A+ grade")
elif(mark<79 and mark>70):
    print("You have A grade")
elif(mark<70 and mark>60):
    print("You have B+ grade")
elif(mark<60 and mark>50):
    print("You have B grade")
elif(mark<50 and mark>40):
    print("You have C grade")
elif(mark<40 and mark>33):
    print("You have D grade")
elif(mark<0):
    print("Invalid Option")
else:
    print("Sorry! You are Fail.")


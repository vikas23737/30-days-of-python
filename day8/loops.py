#1st program display no. from -10 to -1 using for loops
print("Printing number from -10 to -1 using for loop:")
for i in range(-10,0):
    print(i)
    i=i+1

#2nd program display no. in form of matrix 
R=int(input("Enter the number of rows:"))
C=int(input("Enter the number of colounms:"))
matrix=[]
for i in range(R):
    m =[]
    for j in range(C):
        m.append(int(input()))
    matrix.append(m)
for i in range(R):
    for j in range(C):
        print(matrix[i][j],end=" ")
    print()
#3nd program print A one time B two times C 3 times 
for i in range(0,5):
    print(chr(65+i)*(i+1))
    i=i+1

#1st program Take input in tuple and print all its value
tup=(1,2,3,4,5,6)
for i in range(len(tup)):
    print(tup[i],end=' ')

#2nd program sort a tuple of tuples  by its 2 items
tup=[(10,4),(20,9),(30,6),(56,35)]
print("Original tuple:",tup)
tup.sort(key=lambda x:x[1])
print("Sorted tuple",tup)

#3rd program unpack the tuple into 4 variables
*x,y,z= 1,2 ,'King','Poor',
print(x)
print(y)
print(z)
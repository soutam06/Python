n=int(input("Enter the size: "))
space=n
temp=n//2
if (n%2==0):
    size=temp+1 
else:
    size=temp+2

for i in range(size):
    for j in range(n):
        if(i==0 and (j==0 or j==n-1)):
            print(" ",end=" ")
        elif j < i-1:
            print(' ', end=" ")
        elif j > space: 
            print(' ', end=" ")
        else:
            print("*",end=" ")
    space-=1
    print('\n')


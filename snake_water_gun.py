from random import choice
# list=[1,2,3,4,5,6,7]
# print(choice(list))

#  the matrix is            1  2  3   (computer)

#              (u    1      0  1 -1
#               s    2     -1  0  1
#               er)  3      1 -1  0     

#               0=DRAW    1= WIN      -1=LOOSE 

print("**PLEASE NOTE THE RULES THAT**\n1 FOR SNAKE\n2 FOR WATER\n3 FOR GUN\nIF YOU CHOOSE ANY OTHER ELSE THE GAME WILL STOP")
list=[1,2,3]

object=["Snake","Water","Gun"]

result=[["DRAW","YOU WIN","YOU LOOSE"],["YOU LOOSE","DRAW","YOU WIN"],["YOU WIN","YOU LOOSE","DRAW"]]

points=0

while(True):

    ob= int(input("Enter your choice(1,2,3): "))

    if not ob in list:
        break

    print(f"You Choose {object[ob-1]}")
    computer=choice(list)
    # print(computer)

    print(f"Computer Choose {object[computer-1]}")  
    print(f"Result: {result[ob-1][computer-1]}")

    if (result[ob-1][computer-1]=="YOU WIN"):
        points+=2

    if (result[ob-1][computer-1]=="DRAW"):
        points+=1
print(f"Your toal point is {points}")
print("Thankyou For Playing this game!")

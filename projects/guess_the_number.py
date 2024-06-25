from random import randint
a, b = map(int, input("Enter the range separated by a space: ").split())
choice=randint(a,b)
no_of_guess=0
while(True):
    user_input=int(input("Enter your guess: "))
    no_of_guess+=1

    if(choice==user_input):
        break
    elif(choice<user_input):
        print("your guess is too large")
    else:
        print("your guess is too small")
print(f"The number of guess is {no_of_guess}")

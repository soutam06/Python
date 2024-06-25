from random import choice
name=input("Enter your name: ")  #Taking the name form user
print(f"All the best {name} !")  #greeting the participants
  
word_list=['strong','smart','player','cricket',
           'football'] #initializing the list of words
word=choice(word_list)  #choosing a random word form list

guess='' #initializing the guess
no_of_guess=10

while(no_of_guess):  #creating a infinite loop
    fail=0
    ch=input('Enter any character: ')
    guess+=ch
    for i in word:
        if i in guess:
                print(i,end='')
        else:
            print('_',end='')
            fail+=1        
    if(fail==0):
         print(f'You Win!\nThe Correct Word is {word}')        
    if ch not in word:
        no_of_guess-=1
        print(f'Wrong\nYou have remaining {no_of_guess} gusess')
    


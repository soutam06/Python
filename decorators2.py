def decorator(fx):
    def mfx(*name):
        print("Good Evening every one !")
        fx(*name)
    return mfx

@decorator
def print_details(name,age):
    print(f'my name is {name} and my age is {age}')

print_details('soutam','18')    
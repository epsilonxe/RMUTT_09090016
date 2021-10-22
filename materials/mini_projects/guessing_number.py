import random

min_number = 1
max_number = 100
secret_number = random.randint(min_number, max_number)

guess = False

print('GUESSING NUMBER GAME')
print(f'Try to guess my secret number from {min_number} - {max_number} ')

while guess != True:
    x = int(input('Try to guess my number: '))
    if x == secret_number:
        print('Your guess is correct!')
        guess = True
    elif x < secret_number:
        print('Your guessed nunber is too low')
    else:
        print('Your guessed nunber is too high')
        
print('Thanks for playing')

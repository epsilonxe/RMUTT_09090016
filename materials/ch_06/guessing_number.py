correct_number = 3

guess = False
while guess == False:
    n = int(input('Try to guess my number (0-9): '))
    if n == correct_number:
        print('Yes, your guessing is right!')
        guess = True
    else:
        print(f'No, {n} is not correct')

print('Thanks for playing')

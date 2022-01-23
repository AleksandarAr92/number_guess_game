import random


def guess_the_number():
    random_number = random.randint(1, 10)
    max_guess_count = 3

    counter = 0
    print(random_number)
    while counter < max_guess_count:
        user_guess = int(input('Please enter your guess number: '))
        if user_guess == random_number:
            print(f'Well done. You guessed correct')
            break
        elif user_guess < random_number:
            print(f'Your number is lesser than correct number. Please try again')
            counter += 1
        elif user_guess > random_number:
            print(f'Your number is bigger than correct number. Please try again')
            counter += 1


guess_the_number()

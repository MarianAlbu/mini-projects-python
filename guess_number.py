from random import randint
#from art import logo
#print(logo)
#number=randint(1, 100)
#print(number)
#\n
should_continue= True
while should_continue:
    number=randint(1, 100)
    print(number)
    print(' Welcome to the number Guessing Game!')
    difficulty_input=input(" I am thinking of a number between 1 and 100.\n Chose a difficulty.Type 'easy' or 'hard' :")
    attempts=10
    if difficulty_input=='hard':
        attempts =5
    while attempts>0:
        guessed_number=int(input(f' You have {attempts} attempts left.\n Make a guess: '))
        if guessed_number<number:
            print(' Too low.\n Guess again')
        elif guessed_number>number:
            print(' Too high.\n Guess again')
        elif guessed_number==number:
            print(f'You got it! The answer was {number}')
            new_game=input("For new game, type 'y' or 'n' for stop :")
            if new_game == 'n':
                print('See you later')
                should_continue=False
            break
        attempts-=1
        if attempts==0:
            print(f'Game over, the answer was {number}')
            play_game=input("For new game, type 'y' or 'n' for stop :")
            if play_game == 'n':
                print('See you later')
                should_continue=False





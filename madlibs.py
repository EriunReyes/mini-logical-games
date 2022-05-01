# adj = input('adjective:')
# verb1 = input('Verb: ')
# verb2 = input('Verb: ')
# famous_person = input('Famous person:')
# madlib = f'computer programming is {adj}! It woks\
# I love {verb1}. Stay Hidrated and {verb2} Like you are {famous_person}!'
# print(madlib)


# project number 2
import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, guess again.Too low')
#         elif guess == random_number:
#             print(f'Congratulations, you guessed it, it is the number {random_number}')
#         else:
#             print('Sorry, guess again, too high')

# guess(10)

# def computer_guess(x):
#     low = 1
#     high = x  
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low
#         feedback = input(f'Is {guess} too high (H), too low (L),  or correct (C)?? ').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1 

#     print(f'Yay! The computer guessed your number, {guess}, correctly!')

# computer_guess(10)



# Rock, Paper and Scissor
# def play():
#     user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
#     computer = random.choice(['r', 'p', 's'])
#     if user == computer:
#         return 'Tie'
#     if is_win(user, computer):
#         return 'You won'

#     return 'You lost'

# def is_win(player, opponent):
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
#         or (player == 'p' and opponent == 'r'):
#         return True

# print(play())





import random
choice = 'y'
while choice== 'y':
    gestures = ['Rock','Paper','Scissor']
    cpu_choice = random.choice(gestures)
    user_choice = input('Type r for Rock, s for Scissor, and p for Paper: ')
    if user_choice =='r':
        user_choice = 'Rock'
    if user_choice == 's':
        user_choice = 'Scissor'
    if user_choice == 'p':
        user_choice = 'Paper'
#Rock
    if user_choice == 'Rock' and cpu_choice == 'Rock':
        print('You drew Rock, but so did I, so we are cavemen')
    if user_choice == 'Rock' and cpu_choice == 'Scissor':
        print('You won, do no throw the rock in celebration')
    if user_choice == 'Rock' and cpu_choice == 'Paper':
        print('You lost, because the true rock is Dwayne Johnson')
#Scissor
    if user_choice == 'Scissor' and cpu_choice == 'Scissor':
        print('You drew rock, but so did I. There is an adult joke somewhere in there...')
    if user_choice == 'Scissor' and cpu_choice == 'Paper':
        print('You won, go make one of those cut-out snowflakes')
    if user_choice == 'Scissor' and cpu_choice == 'Rock':
        print('You lost, and now you have broken scissors. How do you even break scissors?')
#Paper
    if user_choice == 'Paper' and cpu_choice == 'Paper':
        print('We both drew paper.... We must make paper airplanes now')
    if user_choice == 'Paper' and cpu_choice == 'Rock':
        print('You won, ow you are the proud owner of a paper-covered rock')
    if user_choice == 'Paper' and cpu_choice == 'Scissor':
        print('You lost, at least you gave your opponent a cut_out snowflake')
    choice = input(' Press y to play again, and any other key to exit: ')

import random
play = 'r'
while play == 'r':
#
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10','Jack','Queen','King']
first_card = random.choice(cards)
second_card = random.choice(cards)
#
print(f'Your first card was a(n) {first_card}. The second card was a(n) {second_card}')
#
if first_card == 'Ace' or second_card == 'Ace':
    print('You have drawn an Ace')
    ace_num = input('Type 1 if you want it to equal 1, or type 11 for it to equal 11: ')
    if ace_num == 1 and first_choice == 'Ace':
        first_card = 1
    if ace_num == 11 and first_choice == 'Ace':
        first_card = 11
    if ace_num == 1 and second_choice == 'Ace':
        first_card = 1
    if ace_num == 11 and second_choice == 'Ace':
        first_card = 11
#
if first_card == 'Jack':
    first_card = 10
if second_card == 'Jack':
    second_card = 10
if first_card == 'Queen':
    first_card = 10
if second_card == 'Queen':
    second_card = 10
if first_card == 'King':
    first_card = 10
if second_card == 'King':
    second_card = 10
initial_score = int(first_card) + int(second_card)
print(f'Your two cards have come up to {initial_score}')
if initial_score == 21:
    print(f' Your two cards add up to 21, congratulations!')
    print('Type r to play again
choice = input('Press h to hit (get a new card) or s to stop: ')
if choice == s:
    print
while choice == h:
    

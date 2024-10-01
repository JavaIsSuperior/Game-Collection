import random
choice= 'y'
while choice == 'y':
    word_list=['Tree','Yesterday','Autumn','Cowboy','Lightsaber','Igloo']
    chosen_word = random.choice(word_list)
    print(f'The word is {len(chosen_word)} characters long.')
    choice = 'n'

import random

# Variable declarations
word_list = ['horse', 'truck', 'cloud']
current_word = random.choice(word_list)
blank_word_list = []
blank_word = ''
correct_choice = False
lives = 3
has_char = False

# Display blank word
for x in range(1, len(current_word) + 1):
    blank_word_list.append('_')

# While the word and the blank word are not equal
while current_word != ''.join(blank_word_list):
    # Resets has_char variable
    has_char = False

    # Checks if player is out of lives
    if lives == 0:
        print('You ran out of lives...')
        break

    blank_word = ''.join(blank_word_list)
    print(blank_word)
    print('\nGuess a letter...')
    print(f'Lives left: {lives}\n')

    user_input = input()
    
    # Checks to see if user only guessed one letter
    if len(user_input) > 1:
        print('Please input only one valid letter')
    else:
        print()
        
        # Stops game
        if user_input == 'stop':
            break

        # Checks for users input and if found, replaces space in blank word with letter
        for y in current_word:
            if user_input == y:
                blank_word_list[current_word.find(y)] = y
                print('Correct!')
                has_char = True

            else:
                continue
        
        # Takes away life for incorrect guess
        if not has_char:
            lives -= 1
            print('Incorrect')

if lives > 0:
    print('You Win!!!')
else:
    print('You lose...')
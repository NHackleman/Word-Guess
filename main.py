import random
from bs4 import BeautifulSoup
import requests

# Variable declarations
word_list = []
blank_word_list = []
blank_word = ''
correct_choice = False
lives = 5
has_char = False

user_input = input('How long would you like the word to be? ')

try:
    URL = f"http://www.yougowords.com/{user_input}-letters"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    word_table = soup.find(id='sortable-display')
    results = word_table.find_all('a')

    for result in results:
        word_list.append(result.text.lower())

    current_word = random.choice(word_list)

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

    print(current_word)

except:
    print('Invalid input')
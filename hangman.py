# create a dictionary of words

import random

hangman_dict = [
{
'words': ['chassis', 'engine', 'tires'],
'category': 'cars'
},
{
'words': ['sing', 'flute', 'melody', 'symphony'],
'category': 'music'
}
]
player_name  = 'mer'#input ('Enter your name')
player_score = 0

all_categories = []
for dict in hangman_dict:
    all_categories.append(dict['category'])
print(all_categories)

category_selected = 'cars'#input ('Please select a category: ')
# check input is valid

available_words = []
for dict in hangman_dict:
    if dict["category"] == category_selected:
        available_words = dict['words']

n = random.randint(0,len(available_words) -1)
print(n)

selected_word = available_words[n]
print(selected_word)

len(selected_word)

new_word = []
for char in selected_word:
    new_word.append('_ ') 
print(new_word)

guessed_letters = []

selected_word.split()
max_attempts = 10
current_attempts = 0 

while True:
    #if they ran out of guesses, print a message and quit
    if (current_attempts >= max_attempts):
        print ('You lost!')
        break
    
    guess = input('Enter a letter: ')
    #check if that letter is even in our word. If not, increment the fail count
    if (guess not in selected_word):
        current_attempts += 1
    else:
        #find every place that character should appear, and put it in the masked word
        for index in range(0,len(selected_word)):
            if guess == selected_word[index]:
                new_word[index] = guess
                print (new_word)
        #now that we have plugged in the guessed letter, see if the word is complete. If so, quit
        if '_ ' not in new_word:
            print ('You guessed it!')
            break
            
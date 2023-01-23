import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from a list, in the this case words
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #a SET of all the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #to hold guesses

    lives = 6

#getting user input
    while len(word_letters) > 0 and lives > 0: #len is length
        #letters used (using join imports the list)
        print('You have', lives, 'tries left and these letters have been guessed: ', ' '.join(used_letters))

        #what the current word is with dashes in place of unknows (W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in the word')

        elif user_letter in used_letters:
            print('This letter has already been guessed')
    
        else:
            print('Invalid Character, Guess again')

        #we get here when the lenght of word letters (len(wordletters)) == 0 OR when they die
    if lives == 0:
        print('You ded :(. The word was' ,word)
    else:    
        print ('You guessed the word! It was', word)


hangman()
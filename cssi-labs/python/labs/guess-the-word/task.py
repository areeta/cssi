import random

words = ["python", "javascript", "html", "java", "css",
         "swift", "git", "php", "ruby", "perl"]

# Created a secret word from the list of programming languages
def create_word():
    secret_index = random.randint(0, len(words))
    secret_word = words[secret_index]
    return secret_word

# Finds length of word
comp_word = create_word()
length_of_word = len(comp_word)

# Makes the computer's word into an array
def make_word_as_array():
    word_array = []
    for letter in comp_word:
        word_array.append(letter)
    return word_array

# Makes the user guess into a list
guess_list = list("_" * length_of_word)
guesses = []

# Print functions for the original view, word guess, guesses of user
def print_view():
    for i in range(length_of_word):
        print(guess_list[i]),

def print_guesses():
    for i in range(len(guesses)):
        print(guesses[i]),

def check_if_in_word():
    index_of_letter = comp_word.find(user_guess)
    if(index_of_letter > -1):   #if the letter of the user guess is in the word, then print it
        guess_list[index_of_letter] = user_guess

comp_word_as_list = make_word_as_array()

while comp_word_as_list != guess_list:
    print_view()
    print "Previous guesses: ",
    print_guesses()
    print
    user_guess = input("Guesses: ")
    guesses.append(user_guess)
    check_if_in_word()

print "The word was: " + comp_word

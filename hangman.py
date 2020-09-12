"""Hangman game."""

# from random import choice

# class NewGame:
#     """Game for playing hangman."""

#     def __init__(self):
#         """Initialize variables & create board."""

#         self.turn = 0
#         self.letter_count = 0
#         self.library = {"animals": ["tiger", "lion", "elephant", "flamingo", "gorilla", "kangaroo"], 
#                             "vegetables": ["cucumber", "tomato", "zucchini", "celery", "onion", "carrot"], 
#                             "fruits": ["apple", "pear", "apricot", "grape", "cherry", "mango"],
#                             "music genres": ["pop", "electronic", "hip hop", "jazz", "rock", "latin"]}


#     def hidden_word(self):
#         """User decides a theme and a hidden word is assigned."""

#         userIn = input("What theme would you like your word to be? (animals, vegetables, fruits, music genres)")

#         #Random Animal
#         if userIn == "animals":
#             words = self.library["animals"]
#             hidden_word = choice(words)
#             print(hidden_word)
#         #Random Veggie
#         elif userIn == "vegetables":
#             words = self.library["vegetables"]
#             hidden_word = choice(words)
#             print(hidden_word)
#         #Random Fruit
#         elif userIn == "fruits":
#             words = self.library["fruits"]
#             hidden_word = choice(words)
#             print(hidden_word)
#         #Random Genre
#         elif userIn == "music genres":
#             words = self.library["music genres"]
#             hidden_word = choice(words)
#             print(hidden_word)
#         else:
#             print("Please select a valid theme. Try again.")
#             userIn = input("What theme would you like your word to be? (animals, vegetables, fruits, music genres)")
#             print(userIn)
#             #after the second 
#         self.hidden_word()

#     def print_board(self):
#         """Instructions are told and hidden words empty spaces are shown."""

#         self.letter_count = 0

#         for letter in hidden_word:
#             self.letter_count += 1
        
#         print(self.letter_count * "*")

#         print(self.letter_count)

#         self.print_board()
    
#     def next_turn(self):

# print("Welcome to Hangman!\n\n")
# print("Instructions:\n- Please pick a theme and a random word will be selected\n\n\n")
# hangman_game = NewGame()




# while True:
#     hangman_game.next_turn()



from random import choice

library = {"animals": ["tiger", "lion", "elephant", "flamingo", "gorilla", "kangaroo"], 
                            "vegetables": ["cucumber", "tomato", "zucchini", "celery", "onion", "carrot"], 
                            "fruits": ["apple", "pear", "apricot", "grape", "cherry", "mango"],
                            "music genres": ["pop", "electronic", "hip hop", "jazz", "rock", "latin"]}

hidden_word =""


def hidden_word():
    """User decides a theme and a hidden word is assigned."""

    userIn = input("What theme would you like your word to be? (animals, vegetables, fruits, music genres)")

    #Random Animal
    if userIn == "animals":
        words = library["animals"]
        hidden_word = choice(words)
        print(hidden_word)
    #Random Veggie
    elif userIn == "vegetables":
        words = library["vegetables"]
        hidden_word = choice(words)
        print(hidden_word)
    #Random Fruit
    elif userIn == "fruits":
        words = library["fruits"]
        hidden_word = choice(words)
        print(hidden_word)
    #Random Genre
    elif userIn == "music genres":
        words = library["music genres"]
        hidden_word = choice(words)
        print(hidden_word)
    else:
        print("Please select a valid theme. Try again.")
        userIn = input("What theme would you like your word to be? (animals, vegetables, fruits, music genres)")
        print(userIn)
        #after the second 
    
    letter_count = 0
    # print(hidden_word)

    for letter in hidden_word:
        letter_count += 1
    
    print(f"{letter_count} letters", letter_count * "[_]")


def print_board():
    """Instructions are told and hidden words empty spaces are shown."""


    # print("Welcome to Hangman!\n\n")
    # print("Instructions:\n- Please pick a theme and a random word will be selected\n\n\n")



    letter_count = 0
    # print(hidden_word)

    # for letter in hidden_word:
    #     letter_count += 1
    
    # print(letter_count * "*")

    # print(letter_count)

print_board()
    
    # def next_turn(self):

hidden_word()



#user should input letter guesses 
#set a limit on number of guesses 
#identify hidden word 
#need a function that checks if the guessed letter is in the hidden word 
#check if that letter appears mjultiple times in the hiden word 
# print those letters on the word if it is correct 
#count down a turn if it is incorrect 
# after every turn disable that letter from being guessed again 
# have a list with all the guessed letters 







# What I need 

# display board, player move, next turn, check wins, check winner


# The Goal: Despite the name, the actual “hangman” part isn’t necessary. 
# The main goal here is to create a sort of “guess the word” game. The user needs to be able to input 
# letter guesses. A limit should also be set on how many guesses they can use. This means 
# you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. 
# No need to get too fancy.) You will also need functions to check if the user has actually 
# inputted a single letter, to check if the inputted letter is in the hidden word 
# (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.


# Concepts to keep in mind:

# Random
# Variables
# Boolean
# Input and Output
# Integer
# Char
# String
# Length
# Print


# Likely the most complex project on this list (well, depending on just how 
# intense you went with the adventure text game), the Hangman project 
# compiles the prior concepts and takes them a step further. Here, 
# outcomes are not only determined based on user-inputted data,
#  that data needs to be parsed through, compared, and then either
#  accepted or rejected. If you want to take this project a step further,
#  set up a hangman image that changes!
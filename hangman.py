# stade 7

import random


def get_hint_str():
    mapped_word = map(lambda char: char if char in guessed_letters else '-', word)
    return ''.join(mapped_word)


def single(letter) -> bool:
    if len(letter) == 1:
        return True
    print("You should input a single letter")
    return False


def english_lowercase(letter) -> bool:
    if letter.isalpha() and letter.islower():
        return True
    print("Please enter a lowercase English letter")
    return False


word = random.choice(['python', 'java', 'kotlin', 'javascript'])
guessed_letters = set()
lives = 8
hint = get_hint_str()
print('H A N G M A N')
if input('Type "play" to play the game, "exit" to quit: ') == "exit":
    exit(0)
else:
    while lives > 0:
        print('\n' + hint)
        user_letter = input('Input a letter: ')

        if single(user_letter) and english_lowercase(user_letter):
            if user_letter in guessed_letters:
                print("You've already guessed this letter")
            else:
                if user_letter not in word:
                    print("That letter doesn't appear in the word")
                    lives -= 1
                guessed_letters.add(user_letter)

        hint = get_hint_str()
        if '-' not in hint:
            print(f'''You guessed the word {word}!
    You survived!''')
            break
    else:
        print("You lost!")









# stage 6
# from random import choice
#
# # Pick the random word from list:
#
# word_lst = ['python', 'java', 'kotlin', 'javascript']
# random_word = list(choice(word_lst))
#
# # Create the hint, using "-" where each letter should be
#
# word_guess = "-" * len(random_word)
#
# print("H A N G M A N")
# print()
#
# # How many times have they f'd it up?
#
# failed_attempts = 0
# past_guesses = []
#
# # Play the game
#
# while failed_attempts < 8:
#     print(word_guess)
#     word_guess = list(word_guess)
#     letter_guess = input("Input a letter:")
#     if letter_guess not in set(random_word):
#         print("That letter doesn't appear in the word")
#         failed_attempts += 1
#         if failed_attempts == 8:
#             print("You lost!")
#             exit(0)
#         print()
#         word_guess = "".join(word_guess)
#
#     else:
#         if letter_guess in past_guesses:
#             print("No improvements")
#             failed_attempts += 1
#             if failed_attempts == 8:
#                 print("You lost!")
#                 exit(0)
#         updated_hint = []
#         letter_counter = 0
#         for letter in word_guess:
#             if letter == "-":
#                 if letter_guess != random_word[letter_counter]:
#                     updated_hint.append("-")
#                 else:
#                     updated_hint.append(letter_guess)
#             else:
#                 updated_hint.append(random_word[letter_counter])
#             letter_counter += 1
#         latest_guess = "".join(updated_hint)
#         word_guess = str(latest_guess)
#         repeated_fail_toggle = False
#         print()
#         if word_guess == random_word:
#             print(random_word)
#             print("You guessed the word!")
#             print("You survived!")
#             exit(0)
#     previous_guess = letter_guess
#     past_guesses.append(letter_guess)



# stage 5
# from random import randint
#
#
# def output_word():
#     result_def = ''
#     for elem in word_guess:
#         if elem in symbols:
#             result_def = result_def + elem
#         else:
#             result_def = result_def + '-'
#
#     return result_def
#
#
# word_list = ['python', 'java', 'kotlin', 'javascript']
# word_guess = word_list[randint(0, len(word_list) - 1)]
# tries = 8
# symbols = set()
# print('H A N G M A N')
# while tries > 0:
#     tries -= 1
#     result = output_word()
#     print()
#     print(result)
#     print("Input a letter: ")
#
#     symb = input()
#     if symb in word_guess:
#         symbols.add(symb)
#     elif symb == ' ':
#         pass
#     else:
#         print("That letter doesn't appear in the word")
#         # tries -= 1
#
#     # if tries == 0:
#     #     print("Thanks for playing!\nWe'll see how well you did in the next stage")
#     #     break
#
#     # if '-' not in result:
#     #     print("Thanks for playing!\nWe'll see how well you did in the next stage")
#     #     break
#
# print()
# print("Thanks for playing!\nWe'll see how well you did in the next stage")

# stage 4
# from random import randint
#
# word_list = ['python', 'java', 'kotlin', 'javascript']
# word_guess = word_list[randint(0, len(word_list) - 1)]
# word = input(f'Guess the word {word_guess[0:3] + "-" * (len(word_guess) - 3)}: ')
# if word == word_guess:
#     print('You survived!')
# else:
#     print('You lost!')


# stage 3
# from random import randint
#
# word_list = ['python', 'java', 'kotlin', 'javascript']
# word_guess = word_list[randint(0, len(word_list) - 1)]
# print('H A N G M A N')
# word = input('Guess the word:')
# if word == word_guess:
#     print('You survived!')
# else:
#     print('You lost!')


# stage 2
# word_list = ['python']
# print('H A N G M A N')
# word = input('Guess the word:')
# if word in word_list:
#     print('You survived!')
# else:
#     print('You lost!')


# stage 1
# print('H A N G M A N')
# print('The game will be available soon.')

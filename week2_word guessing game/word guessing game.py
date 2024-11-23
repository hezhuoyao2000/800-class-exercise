"""
1. This is a word guessing game that requires the player to guess the letters contained in the answer word.
2. At the start of the game, the player has 5 life points (HP value)
3. During the game, the player can see 3 types of information (1) the amount of HP remaining,
   (2) the word that is unfully unrevealed , and (3) the letters that have been guessed but are not in the answer.
4. The player can only enter one guessed letter and reveal one letter in the answer at a time
5. When the guess is correct, the game reveals the position of the letter in the answer.
6. If the guessed letter is correct, but the same letter in the answer is not revealed, that letter will not be added to the list of “letters have been tried and not in the answer”.
7. When the guess is wrong, the HP value will be reduced by 1, when the HP value is 0, the game fails and the game is over,
8. guessing the letter right will not restore HP.
9. only if all the letters are guessed before the HP goes to zero will the game be won.
"""



def print_game_state():                     #Show the user the current hp value
                                            #and a portion of the word that has been guessed correctly
                                            #and incorrect letters that have been tried
    print("now HP = ", HP)
    print("word's state now is:"," ".join(display_word))
    print("letters have been tried and not in the word: ", tried_letter,"\n")


def update_display_restpart_word(letter):   #Updating the progress of the game
    for i, char in enumerate(answerword):
        if char == letter and display_word[i] == "_":           # the guessletter is in the answer and still unrevealed
            display_word[i] = letter                            # revealed this letter in the unfinished answer
            restpart_word[i] = "_"                              # cover the right letter position has been guessed
            break

        if letter not in restpart_word:                         #
            tried_letter.append(letter)


import random

print ("this is word guessing game!")
print ("\nyou need to guess which letters are in the word one by one,and enter it.")

wordsLibrary = ["address", "bank", "contract", "digital", "easy", "function"]       # the list of answer words
answerword = random.choice(wordsLibrary)                                            # Randomly pick one from the list as an answer word
restpart_word = list(answerword)

tried_letter = []                                                                   # the letters that have been guessed but are not in the answer.

print(answerword)

HP = 5
display_word = ["_"] * len(answerword)                                              #Initialize the HP and the reveal status of the answer word


while HP > 0:
    print_game_state()                  #show (1) the amount of HP remaining
                                        #(2) the word that is unfully unrevealed
                                        #the letters that have been guessed but are not in the answer.
    guess = input("please enter one letter that you think makes up the word: ").lower()         #input the guess letter

    if guess in tried_letter:                   #If entering a wrong letter that you have already guessed, the HP is still subtracted by one
        print("you have tried this word, guess another one")
        HP -= 1
        print(f"wrong guess, HP - 1, now HP = ", HP)
        continue

    if guess in answerword:
        update_display_restpart_word(guess)     # revealed the letter in the unfinished answer
                                                # cover the right letter position has been guessed
        print("correct")
        if "_" not in display_word:  # If the all letters in the answer have all revealed, the game is declared won
            print("YOU WIN, GAME SUCCESS. the answer is: ", answerword)
            break

    else:                                       #If entering a wrong letter that you have not guessed
        HP -= 1                                 #hp - 1 , and add the letter to the list of wrong letters
        tried_letter.append(guess)
        print(f"wrong guess, HP - 1, now HP = ", HP)

        if HP < 1:  # If HP goes to zero, the game is declared lost
            print("HP RUN OUT, GAME OVER.")



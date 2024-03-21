import os
import time

def find_letters(letter, word):
    for i in range(len(word)):
        if word[i] == letter:
            return i

def won(word):
    os.system("clear")
    print("Congrats, you've won!")
    print(f"The word was {word}")

def lose(word):
    os.system("clear")
    print("You're so bad, you lost!")
    print(f"The word was {word}")

def main():
    os.system('clear')
    word = ""
    lifes = 10
    win = False

    print("Welcome to Hangman!")
    print("Player 1, please enter the word you want to be guessed!")
    
    word = input()
    anon_word = "_" * len(word)

    guessed_letters = []

    while (win is False) and (lifes > 0):
        os.system('clear')
        
        print(f"Not in the word: {guessed_letters}")
        print(f"You have {lifes} lifes left.")
        print(f"{anon_word}")
        print("What is your guess:")
        print("-------------------------------------------------------")

        guess = input()
        amount = 0

        if guess == word:
            won(word)
            win = True
        
        for l in guess:
            if l in word:
                i = find_letters(l, word)
               
                anon_word = list(anon_word)
                anon_word[i] = l
                anon_word = ''.join(anon_word)

            else:
                amount += 1

                if amount == len(guess):
                    lifes -= 1

                if l not in guessed_letters:
                    guessed_letters.append(l)
    
    if win == False:
        lose(word)
                
main()

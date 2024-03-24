import os
import time

HANGMANPICS = ['''
      
      
      
    
      
      
=========''', '''
      +
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def won(word):
    os.system("clear")
    print("Congrats, you've won!")
    print(f"The word was {word}")
    print('''            
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
              ''')

def lose(word):
    os.system("clear")
    print("You're so bad, you lost!")
    print(f"The word was {word}")

def main():
    os.system('clear')
    word = ""
    lifes = 8
    win = False

    print("Welcome to Hangman!")
    print("Player 1, please enter the word you want to be guessed!")
    
    word = input().lower()
    anon_word = "-" * len(word) 
    guessed_letters = []
    hangmanStage = 0

    while (win is False) and (lifes > 0):
        os.system('clear')

        print(f"Not in the word: {guessed_letters}")
        print(f"You have {lifes} chances left.")
        print(HANGMANPICS[hangmanStage])
        print(f"{anon_word}")
        print("\nEnter your guess\n")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        
        guess = ""
        while len(guess) != 1:
            guess = input("Please guess a letter:").lower()
        
        if guess not in word:
            lifes -= 1
            hangmanStage += 1 
            if guess not in guessed_letters:
                guessed_letters.append(guess)
        else:
            list_anon = list(anon_word)
            for i in range(len(list(word))):
                if list(word)[i] == guess:
                    list_anon[i] = guess
            anon_word = "".join(list_anon)

        if anon_word == word:
            won(word)
            win = True
    
    if win == False:
        lose(word)
                
main()
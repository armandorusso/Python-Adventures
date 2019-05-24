import random
import time

hangman = ['''
--------
|      |
       |
       |
       |
       |
    ___|_____ 
''', '''
--------
|      |
o      |
       |
       |
       |
    ___|_____ 
''', '''
--------
|      |
o      |
|      |
       |
       |
    ___|_____ 
''', '''
--------
|      |
o      |
|\     |
       |
       |
    ___|_____ 
    ''', '''
-------
 |     |
 o     |
/|\    |
       |
       |
    ___|_____ 
    ''', '''
-------
 |     |
 o     |
/|\    |
/      |
       |
    ___|_____ 
    ''', '''
-------
 |     |
 o     |
/|\    |
/ \    |
       |
    ___|_____ 
    ''']
words = ['ant', 'rat', 'owl', 'man', 'woman', 'deer', 'antelope', 'friend', 'python', 'snake', 'human', 'marvel', 'steve', 'tony']
guessLetter = []
guess = 0


def midgame(guess, secretword, letter, blankword):
    while guess != len(hangman):
        if letter in secretword:
            if letter in guessLetter:
                print('You already guessed that letter! Enter a new guess: ')
                newLetter = input()
                midgame(guess, secretword, newLetter, blankword)
            print('Nice, you got yourself a correct guess!')
            drawboard(guess, secretword, letter, blankword)
            print('Enter your next guess: ')
            newLetter = input()
            midgame(guess, secretword, newLetter, blankword)
        else:
            if letter in guessLetter:
                print('You guessed that letter already! Enter a new letter: ')
                newerLetter = input()
                midgame(guess, secretword, newerLetter, blankword)
            print('Incorrect guess!')
            guess = guess + 1
            drawboard(guess, secretword, letter, blankword)
            print('You dont have many tries yet! Enter another word: ')
            newerLetter = input()
            midgame(guess, secretword, newerLetter, blankword)


def startgame():
    guess = 0
    print('WELCOME TO HANGMAN!!!!')
    print('We will try to guess a word for you and you will have to guess it!')
    print('We will attempt to guess it now...please wait')
    secretword = words[random.randint(0, len(words)) - 1]
    time.sleep(2)
    print('We got one! Now, what is your first guess?')
    blankword = ['_'] * len(secretword)
    letter = input()
    midgame(guess, secretword, letter, blankword)


def drawboard(guess, secretword, letter, blankword):
    print(hangman[guess])
    i = 0

    guessLetter.append(letter)
    while i != len(secretword):
        if letter == secretword[i]:
            blankword[i] = letter
        i = i+1
    print(blankword)
    print('Your letter guesses so far have been: ')
    print(guessLetter)
    if guess == len(hangman) - 1:
        print('You lose! Play again? Yes: 1   No: 2')
        inp = input()
        if int(inp) == 1:
            guessLetter.clear()
            startgame()
        else:
            exit()
    elif '_' not in blankword:
        print('You guessed the word correctly! The word: ' + secretword)
        print('Play again? Yes: 1   No: 2')
        inp = input()
        if int(inp) == 1:
            guessLetter.clear()
            startgame()
        else:
            exit()





startgame()

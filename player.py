import random
import os

hangman_guess_6 = ("""
      |--------------|\n
      |              |\n                                                            
      |\n
      |\n
      |\n
      |\n
      |\n
     _____________________""")

hangman_guess_5 = ("""
      |--------------|\n
      |              |\n
      |            (o o)\n
      |              |\n
      |\n
      |\n
      |\n
     _____________________""")


hangman_guess_4 = ("""
      |--------------|\n
      |              |\n
      |            (o o)\n
      |              |\n
      |              |\n
      |\n
      |\n
     _____________________""")


hangman_guess_3 = ("""
      |--------------|\n
      |              |\n
      |            (o o)\n
      |           \__|\n
      |              |\n
      |            __|__\n
      |            \n
     _____________________""")


hangman_guess_2 = ("""
      |--------------|\n
      |              |\n
      |            (o o)\n
      |           \__|__/\n
      |              |\n
      |            __|__\n
      |\n
     _____________________""")

hangman_guess_1 = ("""
      |--------------|\n
      |              |\n
      |            (o o)\n
      |           \__|__/\n
      |              |\n
      |            __|__\n
      |           /\n
     _____________________""")


hangman_guess_0 = ("""
      |--------------|\n
      |              |\n
      |            (o o)\n
      |           \__|__/\n
      |              |\n
      |            __|__\n
      |           /     \\\n
     _____________________""")

playerScore = 0
guessesRemaining = 6
warningsRemaining = 3
vowels=["a", "e", "i", "o", "u"]
playerName = ""
secretWords = []
secretWord = ""
highScore = 0
lettersNotGuessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guessedWord = ''

def getHighScoreFromfile():
    f = open('highscore.txt', 'r+')
    r=f.read()
    highScore = int(r)
    if playerScore > highScore:
        s=str(playerScore)
        f.seek(0)
        f.write(s)


def initializeGame():
    f = open('words.txt', 'r')
    r = f.read()
    global secretWords
    secretWords = r.split() #secretwords is the list of 55900 words.
    global highScore
    highScore = getHighScoreFromfile()
    global playerName
    playerName = input("Enter your name: ")
    print()
    print("=====GOOD LUCK!!!=====\n")

def getWordToGuess():
    global secretWord #secretword is the random word selected.
    secretWord = random.choice(secretWords)
    global guessedWord
    guessedWord = "_" * len(secretWord)
    global lettersNotGuessed
    lettersNotGuessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def removeDashWithLetter(enteredAlphabet):
    global guessedWord
    for i in range(len(secretWord)):
        if secretWord[i] == enteredAlphabet:
            guessedWord = guessedWord[:i] + enteredAlphabet + guessedWord[i + 1:]

def showHangMan():
    hangManWithErrors = [hangman_guess_0, hangman_guess_1,hangman_guess_2, hangman_guess_3, hangman_guess_4, hangman_guess_5, hangman_guess_6]
    return hangManWithErrors[guessesRemaining]

def showScreenToPlayer():
    global lettersNotGuessed
    print("======================PLAYER INTERFACE!!======================")
    print("Player Name: ", playerName)
    print("Score: ", playerScore)
    print("High Score: ", highScore)
    print("\nYou have ",guessesRemaining," guesses and ",warningsRemaining," warnings!!")
    print(showHangMan())
    print("\nWord has ", len(secretWord), " alphabets")
    print("\n", guessedWord)
    print("SECRET !!! ", secretWord)
    print("\nREMAINING LETTERS: ", lettersNotGuessed)
    playerAlphabet = input("Enter Letter of your choice !! ").lower()
    removeDashWithLetter(playerAlphabet)
    calculateGuessAndWarning(playerAlphabet)
    calculateplayerScore()
    getHighScoreFromfile()
    if(playerAlphabet in lettersNotGuessed):
        lettersNotGuessed.remove(playerAlphabet)
    playerWinOrLose()


def showPlayerInterface():
    os.system("cls")
    initializeGame()
    getWordToGuess()
    while(guessesRemaining >= 0):
        showScreenToPlayer()
        if "_" not in guessedWord:
            playerShouldContinue = input("Want to try new word ? [Y/N]: ")
            if(playerShouldContinue == "N" or playerShouldContinue == "n"):
                break
            else:
                getWordToGuess()


# secretWord = "Programming"
# uniqueLetters = ""
def getUniqueLetters():
    uniqueLetters = ""
    for alphabet in secretWord:
        if alphabet not in uniqueLetters:
            uniqueLetters += alphabet
    return len(uniqueLetters)

def calculateplayerScore():
    global playerScore
    playerScore = guessesRemaining * getUniqueLetters()
    return playerScore



def calculateGuessAndWarning(playerAlphabet):
    global warningsRemaining
    global guessesRemaining

    if (playerAlphabet not in lettersNotGuessed):
        if warningsRemaining == 0:
            guessesRemaining-=1
        else:
            warningsRemaining-=1
    elif(playerAlphabet not in secretWord):
        if playerAlphabet in vowels:
            guessesRemaining-=2
        else:
            guessesRemaining -= 1

def playerWinOrLose():
    if guessedWord == secretWord:
        print('==========="CONGRAGULATIONS YOU WON!!!"===========\n\n')
    elif (guessesRemaining == 0 or warningsRemaining == 0):
        print('"YOU LOSE :("')
        print('"KEEP TRYING!!"')


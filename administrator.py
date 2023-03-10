
def displayAdminMenu():
    print("=====================ADMINISTRATOR INTERFACE=====================")
    print("1- Add Word")
    print("2- Reset High Score")
    print("3- Return to Main Menu")
    print("E- Exit application")
    adminChoice = input("Enter your choice [1,2,3,E]: ")
    return adminChoice

def addWord():
    print("addWord")
    f = open("words.txt", "r+")
    wordToInsert = input("Enter word to insert: ")
    filedata = f.read()
    wordsList = filedata.split()
    if (wordToInsert not in wordsList):
        f.write(" " + wordToInsert)
        wordsList.append(wordToInsert)
        f.close()
    else:
        print("Word already exists")

def resetScore():
    print("Reset Score")
    f = open("highscore.txt", "w")
    f.write("0")
    f.close()

def showAdminInterface():
    restartApplication = False
    adminMenuChoice = displayAdminMenu()
    if(adminMenuChoice == "1"):
        addWord()
        changes = input("Do you want to make any further changes?[Y/N]: ")
        if (changes == "y" or changes == "Y"):
            showAdminInterface()
        else:
            exit()
    elif(adminMenuChoice == "2"):
        resetScore()
        changes = input("Do you want to make any further changes?[Y/N]: ")
        if (changes == "y" or changes == "Y"):
            showAdminInterface()
        else:
            exit()
    elif(adminMenuChoice == "3"):
        restartApplication = True
    elif(adminMenuChoice == "E"):
        exit()
    else:
        showAdminInterface()
    return restartApplication


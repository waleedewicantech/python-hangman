import administrator
import player

print("========================WELCOME TO HANGMAN=======================\n")
def initialize():
    isAdmin = input("Are you an admin [Y/N]:")
    if(isAdmin == 'Y' or isAdmin == 'y'):
        restartApplication = administrator.showAdminInterface()
        if(restartApplication == True):
            initialize()
    elif(isAdmin == 'N' or isAdmin == 'n'):
        player.showPlayerInterface()
    else:
        print("Wrong choice entered")
        initialize()

initialize()

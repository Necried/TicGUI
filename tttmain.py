import ttthelp as ttt

def main():
    # Display welcome page
    confirm = ttt.MainMenuSetup()
    
    # Proceed to selection page if user clicked on play
    if confirm == True:
        confirm = ttt.SelectionPage()
    else:
        exit(1)

    # Proceed to GamePage, keeping in mind user's choice input
    if confirm == 0:
        ttt.outcome = ttt.GamePage('X')
    elif confirm == 1:
        ttt.outcome = ttt.GamePage('O')

    # Once game is over, proceed to GameOverPage, remembering game outcome
    # Rerun the game or quit based on user input
    if ttt.GameOverPage(ttt.outcome) == 0:
        main()
    else:
        exit(0)
    

if __name__ == "__main__":
    main()

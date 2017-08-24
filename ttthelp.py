## Graphics helper module for the tic tac toe game
## Contains 4 page displays: Main Menu, player selection, game interface and endgame screen

import tictactoe as tic
import pygame
import sys
import time

# import pygame constants
from pygame.locals import *

# pygame.init should be in tttmain.py folder. It's here just for testing purposes.
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize standard font sizes
titleFont = pygame.font.SysFont(None, 56, bold=True)
textFont = pygame.font.SysFont(None, 36)
creditFont = pygame.font.SysFont(None, 24)

# Initialize 'X' and 'O' .png files
xImage = pygame.image.load('X.png')
oImage = pygame.image.load('O.png')

def WindowSetup():
    '''Sets up the pygame interface. Return windowSurface object.'''
    WINDOWWIDTH = 500
    WINDOWHEIGHT = 500
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption("Tic-Tac-Toe")
    windowSurface.fill(WHITE)
    return windowSurface
    
def MainMenuSetup():
    '''Initialize an interactive main menu page.'''
    # Get a windowSurface object to work on
    windowSurface = WindowSetup()
    
    # Create some textboxes to be rendered on the display screen
    TITLE = titleFont.render("TIC TAC TOE", True, BLACK, WHITE)
    TITLERECT = TITLE.get_rect()
    
    CREATOR = textFont.render("By: Lucas!", True, BLUE, WHITE)
    CREATORRECT = CREATOR.get_rect()
    
    CREDITS = creditFont.render("Credit goes to inventwithpython.com for the AI algorithm", True, BLACK, WHITE)
    CREDITSRECT = CREDITS.get_rect()
    
    ENTERBOX = textFont.render("PLAY", True, GREEN, BLACK)
    ENTERBOXRECT = ENTERBOX.get_rect()
    
    EXITBOX = textFont.render("EXIT", True, RED, BLACK)
    EXITBOXRECT = EXITBOX.get_rect()

    # Position each textboxes accordingly onto the screen    
    TITLERECT.centerx = 250
    TITLERECT.centery = 90
    
    CREATORRECT.centerx = 250
    CREATORRECT.centery = 200
    
    CREDITSRECT.centerx = 250
    CREDITSRECT.centery = 290
    
    ENTERBOXRECT.centerx = 167
    ENTERBOXRECT.centery = 400
    
    EXITBOXRECT.centerx = 333
    EXITBOXRECT.centery = 400

    # Create lists of text and the corresponding rectangle objects
    texts = [TITLE, CREATOR, CREDITS, ENTERBOX, EXITBOX]
    rects = [TITLERECT, CREATORRECT, CREDITSRECT, ENTERBOXRECT, EXITBOXRECT]

    for a,b in zip(texts,rects):
        windowSurface.blit(a,b)

    pygame.display.update()

    # Run the event loop
    while True:
        # check for events
        for event in pygame.event.get():
            # Exit if user closes the program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            # Check for user mouse input
            if event.type == MOUSEBUTTONUP:
                # Get current mouse position
                mouse_pos = pygame.mouse.get_pos()
                mouse_posx = mouse_pos[0]
                mouse_posy = mouse_pos[1]
                if mouse_posx >= ENTERBOXRECT.left and mouse_posx <= ENTERBOXRECT.right:
                    if mouse_posy >= ENTERBOXRECT.top and mouse_posy <= ENTERBOXRECT.bottom:
                        pygame.display.quit()
                        return True
                if mouse_posx >= EXITBOXRECT.left and mouse_posx <= EXITBOXRECT.right:
                    if mouse_posy >= EXITBOXRECT.top and mouse_posy <= EXITBOXRECT.bottom:
                        pygame.display.quit()
                        sys.exit()
                        return 0
                    
    
def SelectionPage():
    '''Initialize an 'X'/'O' selection page'''
    # Initialize (another!) pygame window
    windowSurface = WindowSetup()
    
    # Initialize a helper textbox
    HELPER = textFont.render("Select which player you want to play!", True, BLACK, WHITE)
    HELPERRECT = HELPER.get_rect()
    HELPERRECT.centerx = 250
    HELPERRECT.centery = 100

    # Create placeholder rectangles for X and O .png images
    X = pygame.Rect(100, 350, 65, 65)
    O = pygame.Rect(350, 350, 65, 65)
    
    # blit the helper textbox and the two X and O .png images onto the screen
    windowSurface.blit(HELPER, HELPERRECT)
    windowSurface.blit(xImage, X)
    windowSurface.blit(oImage, O)

    pygame.display.update()

    # Run the event loop
    while True:
        # check for events
        for event in pygame.event.get():
            # Exit if user closes the program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Detect and feed input to GamePage function when a player is selected
            if event.type == MOUSEBUTTONUP:
                # Get current mouse position
                mouse_pos = pygame.mouse.get_pos()
                mouse_posx = mouse_pos[0]
                mouse_posy = mouse_pos[1]
                if mouse_posx >= X.left and mouse_posx <= X.right:
                    if mouse_posy >= X.top and mouse_posy <= X.bottom:
                        return 0
                elif mouse_posx >= O.left and mouse_posx <= O.right:
                    if mouse_posy >= O.top and mouse_posy <= O.bottom:
                        return 1
                

def GamePage(playerChoice):
    '''Initialize the game interface'''
    # Initialize (yet another!) pygame window
    windowSurface = WindowSetup()

    # Define a windowgap and spacing constants to make the board interface
    # look neat
    GAP = 40
    SPACING = 140
    CENTER = GAP + SPACING / 2

    # Draw 2 horizontal lines
    pygame.draw.line(windowSurface, BLACK, [GAP, GAP + SPACING], [500 - GAP, GAP + SPACING], 5)
    pygame.draw.line(windowSurface, BLACK, [GAP, GAP + SPACING * 2], [500 - GAP, GAP + SPACING * 2], 5)

    # Draw 2 vertical lines
    pygame.draw.line(windowSurface, BLACK, [GAP + SPACING, GAP], [GAP + SPACING, 500 - GAP], 5)
    pygame.draw.line(windowSurface, BLACK, [GAP + SPACING * 2, GAP], [GAP + SPACING * 2, 500 - GAP], 5)

    pygame.display.update()
    
    # Initialize class Player, based on selection screen choice
    if playerChoice == 'X':
        human = tic.Player('X',0)
        computer = tic.Player('O',1)
    else:
        computer = tic.Player('X',0)
        human = tic.Player('O',1)

    # Pre-define landing squares for MOUSEBUTTONUP
    corners = []
    rowCorners = []
    for row in range(1,4):
        for square in [i * SPACING for i in range(3)]:
            corners.append(rowCorners.append(((GAP + square, GAP + SPACING * (row - 1)),(GAP + square + SPACING, GAP + SPACING * row))))

    # Pre-define landing squares for XO images
    imageCoord = []
    for row in range(3):
        for square in range(3):
            imageCoord.append((CENTER + square * SPACING, CENTER + SPACING * row))

    # Create a dict where key=imageCoords, value=rect object
    imageRender = {}
    for coords in imageCoord:
        placeholder = pygame.Rect(0, 0, 65, 65)
        placeholder.centerx = coords[0]
        placeholder.centery = coords[1]
        imageRender[coords] = placeholder
        
    # Create a dict for key = mouse input and value = board coord
    boardmap = {}
    for a,b in zip(rowCorners,tic.keys):
        dictBuffer = {a: b}
        boardmap.update(dictBuffer)

    # Also create a dict for key=board coord, value=imageCoord
    imageMapping = {}
    for a,b in zip(tic.keys,imageCoord):
        dictBuffer = {a: b}
        imageMapping.update(dictBuffer)

    # Time to start event loop
    while True:
        for event in pygame.event.get():
            # Exit if user closes the program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # initialize board move variable
            move = False
            
            # if Computer's turn
            if computer.myTurn(tic.board) == True:
                time.sleep(1)
                move = tic.make_move(computer,human)

            # else listen for mouse input
            elif event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for k, v in boardmap.items():
                    if mouse_pos[0] > k[0][0] and mouse_pos[0] < k[1][0] and mouse_pos[1] > k[0][1] and mouse_pos[1] < k[1][1]:
                        if human.place(v,tic.board):
                            move = v                            

            # take action when a move is inputed
            if move:
                for k,v in imageMapping.items():
                    if move == k:
                        if not computer.myTurn(tic.board):
                            if computer.get_piece() == 'X':
                                windowSurface.blit(xImage,imageRender[v])
                            else:
                                windowSurface.blit(oImage,imageRender[v])
                        else:
                            if human.get_piece() == 'X':
                                windowSurface.blit(xImage,imageRender[v])
                            else:
                                windowSurface.blit(oImage,imageRender[v])
            
            pygame.display.update()

            # Check if any exit board conditions has occured
            if computer.win(tic.board):
                time.sleep(2)
                pygame.display.quit()
                return 0
            elif human.win(tic.board):
                time.sleep(2)
                pygame.display.quit()
                return 1
            elif tic.legalmoves(tic.board) == []:
                time.sleep(2)
                pygame.display.quit()
                return 2

        
def GameOverPage(outcome):
    # Here comes (another!) pygame window
    windowSurface = WindowSetup()
    
    # Create custom text boxes for each outcome of the game
    if outcome == 0:
        OUTCOME = titleFont.render("NICE TRY!!", True, RED, WHITE)
    elif outcome == 1:
        OUTCOME = titleFont.render("YOU WIN!!", True, GREEN, WHITE)
    elif outcome == 2:
        OUTCOME = titleFont.render("ITS A DRAW...", True, BLUE, WHITE)

    # Create & position the outcome text box
    OUTCOMERECT = OUTCOME.get_rect()
    OUTCOMERECT.centerx = 250
    OUTCOMERECT.centery = 100
    
    # Create another text box asking if player wants to play again
    PROMPT = titleFont.render("Are you playing again?", True, BLACK, WHITE)
    PROMPTRECT = PROMPT.get_rect()
    PROMPTRECT.centerx = 250
    PROMPTRECT.centery = 300
    # Create Yes box
    YES = textFont.render("YES", True, GREEN, BLACK)
    YESRECT = YES.get_rect()
    YESRECT.centerx = 125
    YESRECT.centery = 400

    # Create No box
    NO = textFont.render("NO", True, RED, BLACK)
    NORECT = NO.get_rect()
    NORECT.centerx = 375
    NORECT.centery = 400

    # Create lists of text and the corresponding rectangle objects
    texts = [OUTCOME, PROMPT, YES, NO]
    rects = [OUTCOMERECT, PROMPTRECT, YESRECT, NORECT]

    for a,b in zip(texts,rects):
        windowSurface.blit(a,b)

    pygame.display.update()
    
    # Run the event loop
    while True:
        # check for events
        for event in pygame.event.get():
            # Exit if user closes the program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            # Check for user mouse input
            if event.type == MOUSEBUTTONUP:
                # Get current mouse position
                mouse_pos = pygame.mouse.get_pos()
                mouse_posx = mouse_pos[0]
                mouse_posy = mouse_pos[1]
                if mouse_posx >= YESRECT.left and mouse_posx <= YESRECT.right:
                    if mouse_posy >= YESRECT.top and mouse_posy <= YESRECT.bottom:
                        pygame.display.quit()
                        tic.initial()
                        return 0
                if mouse_posx >= NORECT.left and mouse_posx <= NORECT.right:
                    if mouse_posy >= NORECT.top and mouse_posy <= NORECT.bottom:
                        pygame.quit()
                        sys.exit()
    
        

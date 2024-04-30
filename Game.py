from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MPL import *
from MCL import *
from Board import *
from Paths import *
from GameHelpers import *

import random


W_Width, W_Height = 1500, 1000
# 375 and 250 on either side
BOX_SIZE = 50
POSSIBLE_MOVES_BOXES_COLOR = (0.82, 0.96, 0.96)

## Detections
def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a/2,b/2








# Game Data
players = {
    "yellowPlayer": {
        "tokenColor": (0.75, 0.75, 0.0),
        "tokenPositions": {
            0: (120, 0),
            1: (125, -155),
            2: (155, -125),
            3: (155, -155)
        },
        "tokenPathProgress": {
            0: 53,
            1: None,
            2: None,
            3: None,
        },
        "tokenDocks": {
            0: (125, -125),
            1: (125, -155),
            2: (155, -125),
            3: (155, -155)
        },
        "points": 0,
    },
    "bluePlayer": {
        "tokenColor": (0.0, 0.0, 0.5),
        "tokenPositions": {
            0: (-145, 145),
            1: (-145, 115),
            2: (-115, 145),
            3: (-115, 115)
        },
        "tokenPathProgress": {
            0: None,
            1: None,
            2: None,
            3: None,
        },
        "tokenDocks": {
            0: (-145, 145),
            1: (-145, 115),
            2: (-115, 145),
            3: (-115, 115)
        },
        "points": 0,
    },
    "greenPlayer": {
        "tokenColor": (0.0, 0.5, 0.0),
        "tokenPositions": {
            0: (-145, -125),
            1: (-145, -155),
            2: (-115, -125),
            3: (-115, -155)
        },
        "tokenPathProgress": {
            0: None,
            1: None,
            2: None,
            3: None,
        },
        "tokenDocks": {
            0: (-145, -125),
            1: (-145, -155),
            2: (-115, -125),
            3: (-115, -155)
        },
        "points": 0,
    },
    "redPlayer": {
        "tokenColor": (0.5, 0.0, 0.0),
        "tokenPositions": {
            0: (60, -30),
            1: (125, 115),
            2: (155, 145),
            3: (155, 115),
        },
        "tokenPathProgress": {
            0: 17,
            1: None,
            2: None,
            3: None,
        },
        "tokenDocks": {
            0: (125, 145),
            1: (125, 115),
            2: (155, 145),
            3: (155, 115),
        },
        "points": 0,
    }
}

gameSituation = {
    "safeHomes": [(180, -30), (-180, 30), (-30, -180), (30, 180)],
    "moveSelectionColor": (0.6, 0, 1),
    "turnOrder": ["yellowPlayer", "greenPlayer", "bluePlayer", "redPlayer"],
    "currentTurn": "yellowPlayer",
    "tokensLeft": {
        "yellowPlayer": 4,
        "greenPlayer": 4,
        "bluePlayer": 4,
        "redPlayer": 4
    },
    "selectedToken": None,
    "possibleMovesOriginalColor": [],
    "possibleMoves": [],
    "animationDestination": None,

    "waitingForDiceRoll": True,
    "waitingForTokenSelection": False,
    "waitingForMoveSelection": False,
    "animationIsOngoing": False,
    "diceValue": None,
    "numOfMovesLeft": 0,
}

def onClickDetectTokenSelection(x, y):
    for token in players[gameSituation["currentTurn"]]["tokenPositions"]:
        token_x, token_y = players[gameSituation["currentTurn"]]["tokenPositions"][token]
        if x >= token_x - 15 and x <= token_x + 15 and y >= token_y - 15 and y <= token_y + 15:
            return token
    return None


# Mouse Controller
def mouseListener(button, state, x, y):
    global pos

    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            x, y = convert_coordinate(x, y)
            
            if gameSituation["waitingForTokenSelection"]:
                selectedToken = onClickDetectTokenSelection(x, y)
                if selectedToken is not None and players[gameSituation["currentTurn"]]["tokenPathProgress"][selectedToken] is not None:
                    gameSituation["selectedToken"] = selectedToken
                    
                    changeColorOfPossibleMoves()
                    
                    gameSituation["waitingForTokenSelection"] = False
                    gameSituation["waitingForMoveSelection"] = True
                
                elif selectedToken is not None and players[gameSituation["currentTurn"]]["tokenPathProgress"][selectedToken] is None and gameSituation["numOfMovesLeft"] >= 6:
                    gameSituation["selectedToken"] = selectedToken

                    # Undock token
                    players[gameSituation["currentTurn"]]["tokenPathProgress"][selectedToken] = 0
                    players[gameSituation["currentTurn"]]["tokenPositions"][selectedToken] = paths[gameSituation["currentTurn"] + "Path"][0]
                    gameSituation["numOfMovesLeft"] -= 6
                    gameSituation["selectedToken"] = None

                    if gameSituation["numOfMovesLeft"] > 0:
                        gameSituation["waitingForTokenSelection"] = True
                        gameSituation["waitingForMoveSelection"] = False
                        gameSituation["animationIsOngoing"] = False
                        gameSituation["waitingForDiceRoll"] = False
                    else: 
                        changeTurns()

            elif gameSituation["waitingForMoveSelection"]:
                move = detectClickOnPossibleMove(x, y)
                
                if move is not None:
                    delta = gameSituation["possibleMoves"].index(move)+1
                    gameSituation["numOfMovesLeft"] -= (delta - 1)
                    
                    
                    # Move token
                    players[gameSituation["currentTurn"]]["tokenPathProgress"][gameSituation["selectedToken"]] = players[gameSituation["currentTurn"]]["tokenPathProgress"][gameSituation["selectedToken"]] + delta
                    players[gameSituation["currentTurn"]]["tokenPositions"][gameSituation["selectedToken"]] = paths[gameSituation["currentTurn"] + "Path"][players[gameSituation["currentTurn"]]["tokenPathProgress"][gameSituation["selectedToken"]] - 1]


                    checkOtherPlayerTokens()
                    
                    # Check if token has reached the end
                    if players[gameSituation["currentTurn"]]["tokenPathProgress"][gameSituation["selectedToken"]] == 57:
                        players[gameSituation["currentTurn"]]["points"] += 1
                        if players[gameSituation["currentTurn"]]["points"] == 4:
                            print(f"\n\n\n\n\n**********Player {gameSituation['currentTurn']} has won***********\n\n\n\n\n")
                        

                    # Restore original color of possible moves
                    for move in gameSituation["possibleMoves"]:
                        pier = onClickDetectPier(move[0], move[1])
                        coordinates = onClickDetectCoordinates(move[0], move[1])
                        
                        if pier and coordinates:  #and point < 56
                            board[pier][coordinates][1] = gameSituation["possibleMovesOriginalColor"].pop(0)

                    gameSituation["possibleMovesOriginalColor"] = []


                    if gameSituation["numOfMovesLeft"] == 0:
                        changeTurns()
                    else:
                        # Wait for new token selection
                        gameSituation["waitingForMoveSelection"] = False
                        gameSituation["waitingForTokenSelection"] = True
            



                        
                        

            
        
    if button==GLUT_RIGHT_BUTTON:
        global i, mod
        if state == GLUT_DOWN: 	
            # Dice roll
            if gameSituation["waitingForDiceRoll"]:
                diceValue = [6, 3, 6, 4][i] # random.randint(1, 6)
                i = (i + 1) % mod
                print("Dice Value:", diceValue)
                gameSituation["diceValue"] = diceValue
                gameSituation["numOfMovesLeft"] += diceValue

                if diceValue == 6:
                    return

                if checkPossibilityForMove():
                    gameSituation["waitingForDiceRoll"] = False
                    gameSituation["waitingForTokenSelection"] = True
                else: 
                    changeTurns()


    glutPostRedisplay()

i = 0
mod = 4

def checkOtherPlayerTokens():
    global gameSituation, players
    currentTurn = gameSituation["currentTurn"]

    currentTurnTokenNewPosition = players[currentTurn]["tokenPositions"][gameSituation["selectedToken"]]
    for player in players:
        if player == currentTurn:
            continue
        for token in players[player]["tokenPositions"].keys():
                
                if players[player]["tokenPositions"][token] == currentTurnTokenNewPosition and currentTurnTokenNewPosition not in gameSituation["safeHomes"]:
                    players[player]["tokenPositions"][token] = players[player]["tokenDocks"][token]
                    players[player]["tokenPathProgress"][token] = None
                    # gameSituation["tokensLeft"][player] += 1
                    # print(f"Token {token} of player {player} has been docked")
                # return True
    return False

def changeTurns():
    global gameSituation

    currentTurnIndex = gameSituation["turnOrder"].index(gameSituation["currentTurn"])
    nextTurnIndex = (currentTurnIndex + 1) % 4
    gameSituation["currentTurn"] = gameSituation["turnOrder"][nextTurnIndex]


    gameSituation["selectedToken"] = None
    gameSituation["possibleMoves"] = []
    gameSituation["possibleMovesOriginalColor"] = []
    gameSituation["waitingForMoveSelection"] = False
    gameSituation["numOfMovesLeft"] = 0
    gameSituation["diceValue"] = None
    gameSituation["waitingForTokenSelection"] = False
    gameSituation["animationIsOngoing"] = False
    gameSituation["waitingForDiceRoll"] = True
    print("########### Turn", gameSituation["currentTurn"], "###########\nRight click to roll dice")



def changeColorOfPossibleMoves():
    selectedTokenCurrentPathProgress = players[gameSituation["currentTurn"]]["tokenPathProgress"][gameSituation["selectedToken"]]
    numberOfMoves = gameSituation["numOfMovesLeft"]
    # pathPoints = paths[gameSituation["currentTurn"] + "Path"].keys()[selectedTokenCurrentPathProgress:selectedTokenCurrentPathProgress+numberOfMoves+1]
    end_point = min(56, players[gameSituation["currentTurn"]]["tokenPathProgress"][gameSituation["selectedToken"]]+gameSituation["numOfMovesLeft"])+1

    for point in range(players[gameSituation["currentTurn"]]["tokenPathProgress"][gameSituation["selectedToken"]], end_point):
        pier = onClickDetectPier(paths[gameSituation["currentTurn"] + "Path"][point][0], paths[gameSituation["currentTurn"] + "Path"][point][1])
        coordinates = onClickDetectCoordinates(paths[gameSituation["currentTurn"] + "Path"][point][0], paths[gameSituation["currentTurn"] + "Path"][point][1])
        gameSituation["possibleMoves"].append(paths[gameSituation["currentTurn"] + "Path"][point])
        if pier and coordinates and point < 56:
            gameSituation["possibleMovesOriginalColor"].append(board[pier][coordinates][1])
            board[pier][coordinates][1] = gameSituation["moveSelectionColor"]
    
    # for move in gameSituation["possibleMoves"]:
    #     pier = onClickDetectPier(move[0], move[1])
    #     coordinates = onClickDetectCoordinates(move[0], move[1])
    #     gameSituation["possibleMovesOriginalColor"].append(board[pier][coordinates][1])
    #     board[pier][coordinates] = gameSituation["moveSelectionColor"]


def checkPossibilityForMove():
    global gameSituation, players, paths

    currentTurnTokenProgress = players[gameSituation["currentTurn"]]["tokenPathProgress"]
    
    # Checking if there are undocked tokens
    for token in currentTurnTokenProgress:
        if currentTurnTokenProgress[token] is not None:
            break
        return False if gameSituation["numOfMovesLeft"] < 6 else True
    
    # Checking if token has enough path to be covered
    for token in currentTurnTokenProgress:
        if token + gameSituation["numOfMovesLeft"] <= 56:
            return True
    return False
        
def detectClickOnCurrentTurnToken(x, y):
    global gameSituation, players
    currentTurn = gameSituation["currentTurn"]
    for token in players[currentTurn]["tokenPositions"]:
        token_x, token_y = players[currentTurn]["tokenPositions"][token]
        if x >= token_x - 15 and x <= token_x + 15 and y >= token_y - 15 and y <= token_y + 15:
            return token
    return None

def detectClickOnPossibleMove(x, y):
    global gameSituation, players
    currentTurn = gameSituation["currentTurn"]
    for move in gameSituation["possibleMoves"]:
        move_x, move_y = move
        if x >= move_x - 15 and x <= move_x + 15 and y >= move_y - 15 and y <= move_y + 15:
            return move
    return None

# Drawing Functions
def drawTokens():
    for key in players:
        tokenColor = players[key]["tokenColor"]
        tokenPositions = players[key]["tokenPositions"]
        glColor3f(tokenColor[0], tokenColor[1], tokenColor[2])
        for token in tokenPositions:
            x, y = tokenPositions[token]
            MCL(x, y, 10)


def drawBox(center, size, color): # Draw a cross at the top right
    glColor3f(0, 0, 0)
    x, y = center
    s = size // 2

    MPL(x+s, y+s, x+s, y-s)
    MPL(x+s, y-s, x-s, y-s)
    MPL(x-s, y-s, x-s, y+s)
    MPL(x-s, y+s, x+s, y+s)

    fill(color, center, size)

def fill(color, center, size):
    x, y = center
    s = size // 2
    r, g, b = color
    glColor3f(r, g, b)

    y_max = y + s
    y_min = y - s
    x_max = x + s
    x_min = x - s

    # Color left and bottom edges
    # First loop leaves out y_max and includes y_min
    y = y_max-0.5
    x = x_min+0.5
    while y > y_min: 
        while x < x_max:
            glBegin(GL_POINTS)
            glVertex2d(x, y)
            glEnd()
            x += 0.5
        x = x_min+0.5
        y -= 0.5


def drawBoard():
    for pier in board.keys():
        if pier in ["pierHorizontalRight", "pierHorizontalLeft", "pierVerticalTop", "pierVerticalBottom"]:
            for key in board[pier].keys():
                color = board[pier][key][1]
                center = board[pier][key][0]
                drawBox(center, 30, color)
        else: 
            for key in board[pier].keys():
                if key == (0, 0):
                    color = board[pier][key][1]
                    center = board[pier][key][0]
                    drawBox(center, 180, color)
                else: 
                    color = board[pier][key][1]
                    center = board[pier][key][0]
                    drawBox(center, 120, color)












def display():
    global pos
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    
    glClearColor(1,1,1,1);	# WHITE BACKGROUND
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    

    drawBoard()
    drawTokens()

    # Game controls

    # if gameSituation["numOfMovesLeft"] > 0:
    #     gameSituation["waitingForTokenSelection"] = True

    # elif gameSituation["waitingForTokenSelection"]:
    #     print("Select token")

    glutSwapBuffers()

pos = 0
         # player color   # token pos  #token num
# players["yellowPlayer"]["tokenPositions"][0] = paths["yellowPlayerPath"][1]
def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global pos, players, paths, gameSituation

    # if animationIsOngoing:
    #     if pos <= 56:
    #         players["yellowPlayer"]["tokenPositions"][0] = paths["yellowPath"][pos]
    #         players["greenPlayer"]["tokenPositions"][0] = paths["greenPath"][pos]
    #         players["bluePlayer"]["tokenPositions"][0] = paths["bluePath"][pos]
    #         players["redPlayer"]["tokenPositions"][0] = paths["redPath"][pos]
    #         pos += 1
    # print(pos)
    
    
        

def init():
    #//clear the screeng
    global pos
    pos = 0
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104, 1.5, 1,	1500.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance
    print(f"########### Turn {gameSituation['currentTurn']} ###########\nRight click to roll dice")


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Ludo project")
init()

glutDisplayFunc(display)	# Display callback function
glutIdleFunc(animate)	# What you want to do in the idle time (when no drawing is occuring)
glutMouseFunc(mouseListener)

# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL












import random

##############################
# Full name: Maxim Melkonian #
# Student number:  300019652 #
# Course: IT1 1120           #
# Assignment Number: 3       #
##############################


############################################
#       Additional Helper Functions        #
############################################

def clear_Screen():
    """Clears screen by adding 50 newlines which is the height of the python shell"""
    print("\n"*50)
    
def ascii_name_plaque(name: str):
    """Creates an asterisk-based plaque using the print command"""
    inputLength = len(name)
    print("*" * (inputLength + 10))
    print("*" + (" " * (inputLength + 8)) + "*")
    print("*" + (" " * 2) + "__" + name + "__" + (" " * 2) + "*")
    print("*" + (" " * (inputLength + 8)) + "*")
    print("*" * (inputLength + 10))

###################################################################################################
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    print("Shuffling deck...")
    tempBoard = deck[:]
    length = len(tempBoard)
    for i in range(length):
        temp = random.randrange(len(tempBoard))
        deck[i] = tempBoard[temp]
        tempBoard.pop(temp)

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    temp = discovered[:]
    temp[p1-1] = original_board[p1-1]
    temp[p2-1] = original_board[p2-1]
    print_board(temp)

#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    # YOUR CODE GOES HERE
    i=0
    while i!=len(l):
        if l[i]=='*' or l.count(l[i])%2:
            l.pop(i)
        else:
            playable_board+=l[i]
            i+=1
    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE
    for i in range(len(l)):
        if l.count(l[i])!=2:
            return False
    return True
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the function that plays the game
    # YOUR CODE GOES HERE
    guesses=0
    hiddenList = list("*"*len(board))
    while hiddenList!=board:
        print_board(hiddenList)
        print("\n")
        pos1,pos2=0,0
        while pos1==pos2 or hiddenList[pos1-1] == board[pos1-1] or hiddenList[pos2-1] == board[pos2-1]:
            print("\nEnter two distinct positions positions on the board that you want revealed.\ni.e two integers in the range [1," + str(len(hiddenList)) + "]")
            pos1 = int(input("Enter position 1: "))
            pos2 = int(input("Enter position 2: "))
            if hiddenList[pos1-1] == board[pos1-1] or hiddenList[pos2-1] == board[pos2-1]:
                print("One or both of your positions has/have already been paired")
            if pos1==pos2:
                print("You chose the same position")
            if pos1==pos2 or hiddenList[pos1-1] == board[pos1-1] or hiddenList[pos2-1] == board[pos2-1]:
                print("Please try again. Your guess did not count. Your current number of guesses is " + str(guesses))
        print_revealed(hiddenList,pos1,pos2,board)
        wait_for_player()
        if board[pos1-1] == board[pos2-1]:
            hiddenList[pos1-1] = board[pos1-1]
            hiddenList[pos2-1] = board[pos2-1]
        guesses+=1
        clear_Screen()
    if guesses>len(hiddenList)//2:
        print("Congratulations! You completed the game with " + str(guesses) + " guesses. That is " + str(guesses-(len(hiddenList)//2))+ " more than the possible best")
    else:
        print("Congratulations! You completed the game with " + str(guesses) + " guesses. That is the possible best!")
        
#main
        
ascii_name_plaque("Welcome to the Concentration game")
print("\n\n")

#YOUR CODE TO GET A CHOICE 1 or CHOICE 2 from a player GOES HERE

userChoice = int(input("Would you like (enter 1 or 2 indicate your choice): \n (1) me to generate a rigorous deck of cards for you \n (2) or, would you like me to read a deck from a file?\n"))
if userChoice!=1 and userChoice!=2:
    while userChoice!=1 and userChoice!=2:
        userChoice= int(input((str(userChoice) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice\n")))    

# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)

if userChoice==1:
    print("You chose to have a rigorous deck generated for you\n")
    size = int(input("\nHow many cards do you want to play with?\nEnter an even number between 0 and 52: ")) 
    if size<0 or size>52 or size%2:
        while size<2 or size>52 or size%2:
            size = int(input("\nHow many cards do you want to play with?\nEnter an even number between 0 and 52: "))
    board = create_board(size)
    shuffle_deck(board)
    clear_Screen()
    if len(board)==0:
        print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGoodbye")
    else:
        play_game(board)

# YOUR CODE FOR OPTION 2 GOES HERE

if userChoice==2:
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    cleaned_board=clean_up_board(board)
    if is_rigorous(cleaned_board):
        ascii_name_plaque("This deck is now playable and is rigorous and has " + str(len(cleaned_board)) + " cards.")
    else:
        ascii_name_plaque("This deck is now playable but not rigorous and it has " + str(len(cleaned_board)) + " cards.")
    wait_for_player()
    clear_Screen()
    shuffle_deck(cleaned_board)
    wait_for_player()
    clear_Screen()
    if len(cleaned_board)==0:
        print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGoodbye")
    else:
        play_game(cleaned_board)
    


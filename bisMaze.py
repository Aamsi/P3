from random import randrange
from maze import maze

class Character:
    """Character : 
       - MacGyver (position and inventory)
       - Guardian (position and inventory = 0)"""
    
    """Two attributes: position and inventory"""
    def __init__(self, position_x, position_y, inventory):
        self.position_x = position_x
        self.position_y = position_y
        self.inventory = inventory

class Item:
    """#Item:
       - Niddle
       - Tube
       - Ether
       Each have one attribute: position"""

    def __init__(self, nom, position=[]):
        self.nom = nom
        self.position = position


def path(macGyver, maze, initial_position):
    """check if the coordonnates of MG == coordonnates of the path on x"""

    try:
        if maze[macGyver.position_y][macGyver.position_x] == '0' or macGyver.position_x == -1 or macGyver.position_y == -1:
            macGyver.position_x = initial_position[0]
            macGyver.position_y = initial_position[1]
            print("Vous ne pouvez pas aller là")

    except IndexError:
        print("Vous ne pouvez pas allez là")
        macGyver.position_x = initial_position[0]
        macGyver.position_y = initial_position[1]
    
def ask_input():
    """ask input to the user"""

    can_move = False

    while not can_move:
        move = input("Right: d\nLeft: q\nUp: z\nDown: s\n")
        
        if move != "s" and move != "d" and move != "z" and move != "q":
            can_move = False
            print("Vous n'avez pas entré les touches de direction")
        else:
            can_move = True
    
    return move
    
def movement(macGyver):
    """movement method: ask the user to press z, q, s or d to move and return macGyver's position += 1"""

    position = [macGyver.position_x, macGyver.position_y]
    move = ask_input()
       
    if move == "d":
        macGyver.position_x += 1
        position[0] = macGyver.position_x
    elif move == "q":
        macGyver.position_x -= 1
        position[0] = macGyver.position_x
    elif move == "z":
        macGyver.position_y -= 1
        position[1] = macGyver.position_y
    elif move == "s":
        macGyver.position_y += 1
        position[1] = macGyver.position_y
   
    return position

def get_object(macGyver, Item): 
    """If Mac Gyver position == Object position, add 1 to MacGyver inventory"""

    macGyver.inventory += 1
    picked_up(Item)
    return macGyver.inventory

def check_guardian(macGyver, guardian):
    """Check if MacGyver's in front of the guardian:"""

    finished = False
    x_finished = check_x_position(macGyver, guardian)
    y_finished = check_y_position(macGyver, guardian)

    if x_finished and y_finished:
        finished = True
    else:
        finished = False

    return finished

def win_lose(macGyver, guardian):
    finished = check_guardian(macGyver, guardian)
    inventory = macGyver.inventory
    
    win = False
    if finished and inventory == 3:
        win = True
    elif finished and inventory != 3:
        win = False
        print("Vous n'avez pas assez d'objets pour tuer le guardien!")

    return win

def check_x_position(macGyver, guardian):
    x_finished = False

    if macGyver.position_x == guardian.position_x:
        x_finished = True
    else:
        x_finished = False
    
    return x_finished

def check_y_position(macGyver, guardian):
    y_finished = False

    if macGyver.position_y == guardian.position_y:
        y_finished = True
    else:
        y_finished = False
    
    return y_finished

def picked_up(Item):
    Item.position = [-100, -100]

def random_pos(maze):
    x = 0
    pos = []
    pos_rand = [0, 0]

    while x < 15:
        y = 0

        while y < 15:
            if maze[y][x] == "1":
                pos_rand = [x, y]
                pos.append(pos_rand)
            y += 1
        x += 1

    i = randrange(len(pos))
    coord = pos[i]

    return coord
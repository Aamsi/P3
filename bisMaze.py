class Character:
    #Character : 
    #   - MacGyver (position and inventory)
    #   - Guardian (position and inventory = 0)
    
    #Two attributes: position and inventory
    def __init__(self, position_x, position_y, inventory):
        self.position_x = position_x
        self.position_y = position_y
        self.inventory = inventory

class Item:
    #Item:
    #   - Niddle
    #   - Tube
    #   - Ether
    #Each have one attribute: position

    def __init__(self, nom, position_x, position_y, position = []):
        self.nom = nom
        self.position_x = position_x
        self.position_y = position_y
        self.position = [self.position_x, self.position_y]


#check if the coordonnates of MG == coordonnates of the path on x
def path(macGyver, maze, initial_position):
    try:
        if maze[macGyver.position_y][macGyver.position_x] == '0' or macGyver.position_x == -1 or macGyver.position_y == -1:
            macGyver.position_x = initial_position[0]
            macGyver.position_y = initial_position[1]
            print("Vous ne pouvez pas aller là")
    except IndexError:
        print("Vous ne pouvez pas allez là")
        macGyver.position_x = initial_position[0]
        macGyver.position_y = initial_position[1]
    
#ask input to the user
def ask_input():
    can_move = False

    while can_move == False:
        move = input("Right: d\nLeft: q\nUp: z\nDown: s\n")
        
        if move != "s" and move != "d" and move != "z" and move != "q":
            can_move = False
            print("Vous n'avez pas entré les touches de direction")
        else:
            can_move = True
    
    return move
    
#movement method: ask the user to press z, q, s or d to move and return macGyver's position += 1
def movement(macGyver):
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

#If Mac Gyver position == Object position, add 1 to MacGyver inventory
def get_object(macGyver, Item): 
    macGyver.inventory += 1
    picked_up(Item)
    return macGyver.inventory

#Check if MacGyver's in front of the guardian:
def check_guardian(macGyver, guardian):
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
    if finished == True and inventory == 3:
        win = True
    elif finished == True and inventory != 3:
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

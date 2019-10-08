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

class Maze:
    #Create two attributes: one for x coordonnates and one for y coordonnates
    def __init__(self, list_x, list_y):
        self.list_x = list_x
        self.list_y = list_y




#check if the coordonnates of MG == coordonnates of the path on x
def path(macGyver, maze, i, position_init):
    path_x = False
    path_y = False
    path = False

    if macGyver.position_x == maze.list_x[i]:
        path_x = True
    else:
        path_x = False
        macGyver.position_x = position_init[0]

    if macGyver.position_y == maze.list_y[i]:
        path_y = True
    else:
        path_x = False
        macGyver.position_y = position_init[1]
    
    if not path_x or not path_y:
        path = False
        print("Vous ne pouvez pas aller là, il y a un mur!")
    else:
        path = True
    
    return path
    


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
        macGyver.position_x += 1.0
        position[0] = macGyver.position_x
    elif move == "q":
        macGyver.position_x -= 1.0
        position[0] = macGyver.position_x
    elif move == "z":
        macGyver.position_y += 1.0
        position[1] = macGyver.position_y
    elif move == "s":
        macGyver.position_y -= 1.0
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

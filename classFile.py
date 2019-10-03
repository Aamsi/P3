class Characters:
    #characters : 
    #   - MacGyver (position and inventory)
    #   - Guardian (position and inventory = 0)
    
    #Two attributes: position and inventory
    def __init__(self, position, inventory):
        self._position = position
        self._inventory = inventory
    
    #To get the current position of the character
    def _get_position(self):
        return self._position
    
    #To set the new position of the character
    def _set_position(self, new_position):
        self._position = new_position
        return new_position
    
    def _get_inventory(self):
        return self._inventory

    #If Character gets an item, it adds 1 to its inventory
    def _set_inventory(self, new_inventory):
        self._inventory = new_inventory
        return new_inventory

    position = property(_get_position, _set_position)
    inventory = property(_get_inventory, _set_inventory)

class Objects:
    #Objects:
    #   - Niddle
    #   - Tube
    #   - Ether
    #Each have one attribute: position

    def __init__(self, nom, position):
        self.nom = nom
        self._position = position
    
    def _set_position(self, new_position):
        self.position = new_position
    
    def _get_position(self):
        return self._position
    
    position = property(_get_position, _set_position)

#movement method: ask the user to press s to move forward and return macGyver's position
def movement(macGyver):
    can_move = False
    while can_move == False:
        move = input("Pour avancer, appuyez sur s: ")
        if move == "s":
            macGyver.position += 1.0
            can_move = True
        else:
            print("Vous n'avez pas appuyé sur s")
            can_move = False
    return macGyver.position

#If Mac Gyver position == Object position, add 1 to MacGyver inventory
def get_object(macGyver): 
    macGyver.inventory += 1
    return macGyver.inventory

#Check if MacGyver's in front of the guardian:
def check_guardian(macGyver, guardian):
    finished = False

    if macGyver.position == guardian.position:
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

    return win


    


from bisMaze import (Character, Item, movement, get_object, check_guardian,
                    win_lose, path, random_pos)                   
from maze import maze

"""I create all my Items:"""

"""Character have a position and an inventory"""
macGyver = Character(5, 0, 0)
guardian = Character(5, 14, 0)

"""Item just have a position"""
niddle = Item("Aiguille", random_pos(maze))
tube = Item("Tube en plastique", random_pos(maze))
ether = Item("Ether", random_pos(maze))
print("Aiguille", niddle.position)
print("Tube", tube.position)
print("Ether", ether.position)

"""I put my Item in a list so I can iterate whenever MacGyver moves to check if
   an object is here"""
Items = [niddle, tube, ether]

"""I create two var for position and inventory so it's clearer"""
position = [macGyver.position_x, macGyver.position_y]
player_inventory = macGyver.inventory

finished = False

"""Ask the user to move if he's not in front of the guardian""" 
while not finished:

    """We register initial coordonnates to apply in path parameter"""
    position_init = [macGyver.position_x, macGyver.position_y]

    """We call the method movement to add 1 to MacGyver's inventory"""
    position = movement(macGyver)
    print("Position avant vérif", position)

    """Check if he's on the wall"""
    path(macGyver, maze, position_init)
    
    print("Coordonnées après vérif", macGyver.position_x, macGyver.position_y)
    
    """"Once he moved, check if there's an object and/or if he is at the end,
        if not, movement()"""
    for objet in Items:

        """"If there's an object, add 1 to the inventory"""
        if position == objet.position:
            player_inventory = get_object(macGyver, objet)
            print("Vous avez rammassé: {}".format(objet.nom))
            print("Vous avez {} objet(s) dans votre inventaire"
                  .format(player_inventory))

    """check if he's in front of the guardian"""
    finished = check_guardian(macGyver, guardian)

"""check if he won after finished is True"""
win = win_lose(macGyver, guardian)
if win:
    print("Bravo! Vous avez gagné")
else:
    print("Désolé, vous avez perdu!")









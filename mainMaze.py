from bisMaze import Character, Item, Maze, movement, get_object, check_guardian, win_lose, path
from maze import LIST_X, LIST_Y

#I create all my Items:

maze = Maze(LIST_X, LIST_Y)

#Character have a position and an inventory
macGyver = Character(7.0, 2.0, 0)
guardian = Character(7.0, 15.0, 0)

#Item just have a position
niddle = Item("Aiguille", 4.0, 10.0)
tube = Item("Tube en plastique", 7.0, 6.0)
ether = Item("Ether", 9.0, 9.0)

#I put my Item in a list so I can iterate whenever MacGyver moves to check if an object is here
Items = [niddle, tube, ether]

#I create two var for position and inventory so it's clearer
position = [macGyver.position_x, macGyver.position_y]
player_inventory = macGyver.inventory

#An iteration to check for the coordonnates
i = 1

finished = False
#Ask the user to move if he's not in front of the guardian 
while finished == False:

    #We register initial coordonnates to apply in path parameter
    position_init = [macGyver.position_x, macGyver.position_y]

    #We call the method movement to add 1 to MacGyver's inventory
    position = movement(macGyver)
    print("Position ", position)

    #Check if he's on the wall or not, if he can move, i += 1
    valid_move = path(macGyver, maze, i, position_init)
    if valid_move:
        i += 1
    
    print("Coordonnées après vérif", macGyver.position_x, macGyver.position_y)
    
    #Once he moved, check if there's an object and/or if he is at the end, if not, movement()
    for objet in Items:

        #If there's an object, add 1 to the inventory
        if position == objet.position:
            player_inventory = get_object(macGyver, objet)
            print("Vous avez rammassé: {}".format(objet.nom))
            print("Vous avez {} objet(s) dans votre inventaire".format(player_inventory))

    #check if he's in front of the guardian
    finished = check_guardian(macGyver, guardian)

#check if he won after finished is True
win = win_lose(macGyver, guardian)
if win == True:
    print("Bravo! Vous avez gagné")
else:
    print("Désolé, vous avez perdu!")









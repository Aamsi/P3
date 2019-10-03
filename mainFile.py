from classFile import Characters, Objects, movement, get_object, check_guardian, win_lose

#I create all my objects:

#Characters have a position and an inventory
macGyver = Characters(0.0, 0)
guardian = Characters(10.0, 0)

#Objects just have a position
niddle = Objects("Aiguille", 1.0)
tube = Objects("Tube en plastique", 4.0)
ether = Objects("Ether", 6.0)

#I put my objects in a list so I can iterate whenever MacGyver moves to check if an object is here
objects = [niddle, tube, ether]

#I create two var for position and inventory so it's clearer
position = macGyver.position
player_inventory = macGyver.inventory

finished = False
#Ask the user to move if he's not in front of the guardian 
while finished == False:

    #We call the method movement to add 1 to MacGyver's inventory
    position = movement(macGyver)
    
    #Once he moved, check if there's an object and/or if he is at the end, if not, movement()
    for objet in objects:

        #If there's an object, add 1 to the inventory
        if position == objet.position:
            player_inventory = get_object(macGyver)
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









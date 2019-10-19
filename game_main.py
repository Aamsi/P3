import pygame as pg

from gamebis import Character, Item, Maze, sprite_print, inventory_counter, win_sprite

win = False
while win == False:
    """Maze"""
    maze = Maze('Maze.txt')
    maze_struct = maze.loadmaze()

    """Characters"""
    macgyver = Character(5, 0, 0)
    guardian = Character(5, 14, 0)

    """MacGyver's position and inventory"""
    hero_position = [macgyver.position_x, macgyver.position_y]
    hero_inventory = macgyver.inventory

    """Items"""
    niddle = Item("Aiguille", maze.random_pos())
    tube = Item("Tube en plastique", maze.random_pos())
    ether = Item("Ether", maze.random_pos())

    """Items list"""
    items = [niddle, tube, ether]

    #PG
    pg.init()
    screen = pg.display.set_mode((600, 600), pg.RESIZABLE)

    continuer = True

    while continuer:
        pg.draw.rect(screen, (0, 0, 0), (0, 0, 600, 600))

        """Passive objects"""
        sprite_print(guardian, 'ressource/Gardien.png', screen)
        sprite_print(niddle, 'ressource/aiguille.png', screen)
        sprite_print(tube, 'ressource/tube_plastique.png', screen)
        sprite_print(ether, 'ressource/ether.png', screen)

        """Display the maze interface"""
        maze.maze_interface(screen)

        """Display the counter sprite"""
        inventory_counter(macgyver, screen)

        """Keep initial MacGyver's position in memory"""
        initial_pos = [macgyver.position_x, macgyver.position_y]

        """Modifying MacGyver position"""
        hero_position = macgyver.movement()

        """Check if he moves toward a wall"""
        macgyver.path(maze_struct, initial_pos)

        """Display MacGyver"""
        sprite_print(macgyver, 'ressource/MacGyver.png', screen)

        """Check if he's on an item, if so, add 1 to inventory"""
        for item in items:
            if hero_position == item.position:
                hero_inventory = macgyver.get_object(item)
                print(hero_inventory)
        
        """Check if MacGyver's in front of the guardian"""
        finished = macgyver.check_guardian(guardian)
        
        """Check if he fills all conditions and if he wins"""
        if finished:
            win = macgyver.win_lose(guardian)
            win_sprite(screen, win)
            continuer = False
        
        pg.display.flip()
    #PG


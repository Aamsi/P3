import pygame as pg
from time import sleep

from core import (Character, Item, Maze, sprite_interaction, 
                     inventory_counter_sprite, win_sprite)


win = False

"""If user wins, close the program, else, keep running"""
while win == False:

    """Maze"""
    maze = Maze('level0.txt')
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

    """Pygame loop"""
    pg.init()
    screen = pg.display.set_mode((600, 600), pg.RESIZABLE)
    pg.display.set_caption("THE MAZE")

    continuer = True
    """Run the game while user doesn't press ESCAPE to quit or user's not in
        front of the guardian"""
    while continuer:
        pg.draw.rect(screen, (0, 0, 0), (0, 0, 600, 600))

        """Passive objects"""
        sprite_interaction(guardian, 'ressource/Gardien.png', screen)
        sprite_interaction(niddle, 'ressource/aiguille.png', screen)
        sprite_interaction(tube, 'ressource/tube_plastique.png', screen)
        sprite_interaction(ether, 'ressource/ether.png', screen)

        """Display the maze interface"""
        maze.maze_interface(screen)

        """Display the counter sprite"""
        inventory_counter_sprite(macgyver, screen)

        """Keep initial MacGyver's position in memory"""
        initial_pos = [macgyver.position_x, macgyver.position_y]

        """Modifying MacGyver position with inputs"""
        hero_position = macgyver.movement()

        """Check if he moves towards a wall"""
        macgyver.path(maze_struct, initial_pos)

        """Display MacGyver"""
        sprite_interaction(macgyver, 'ressource/MacGyver.png', screen)

        """Check if he's on an item, if so, add 1 to inventory"""
        for item in items:
            if hero_position == item.position:
                hero_inventory = macgyver.get_object(item)
        
        """Check if MacGyver's in front of the guardian"""
        finished = macgyver.check_guardian(guardian)
        
        """Check if he fills all conditions and if he wins"""
        if finished:
            win = macgyver.win_lose(guardian)
            win_sprite(screen, win)
            continuer = False
            """Display loosing or winning sprite"""
            pg.display.flip()
            sleep(2)

        pg.display.flip()


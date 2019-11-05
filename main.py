from time import sleep
import pygame as pg

from core import (Character, Item, Maze, load_counter_sprite, win_sprite,
                  load_image, draw_sprite)


win = False
"""If user wins or close the program, else, keep running"""
while not win:

    """Maze"""
    maze = Maze('level0.txt')
    start_position = maze.start()
    end_position = maze.end()

    """Characters"""
    macgyver = Character(start_position[0], start_position[1], 0)
    guardian = Character(end_position[0], end_position[1], 0)

    """Items"""
    niddle = Item("Aiguille")
    niddle.random_pos(maze.struct)
    tube = Item("Tube en plastique")
    tube.random_pos(maze.struct)
    ether = Item("Ether")
    ether.random_pos(maze.struct)

    """Items list"""
    items = [niddle, tube, ether]

    """Pygame loop"""
    pg.init()
    screen = pg.display.set_mode((600, 600), pg.RESIZABLE)
    pg.display.set_caption("THE MAZE")

    """Load sprites"""
    macgyver_sprite = load_image('ressource/MacGyver.png')
    guardian_sprite = load_image('ressource/Gardien.png')
    niddle_sprite = load_image('ressource/aiguille.png')
    ether_sprite = load_image('ressource/ether.png')
    tube_sprite = load_image('ressource/tube_plastique.png')
    counters = load_counter_sprite(macgyver)

    keep_going = True
    """Run the loop while user doesn't press ESCAPE to quit or user's not in
        front of the guardian"""
    while keep_going:
        pg.draw.rect(screen, (0, 0, 0), (0, 0, 600, 600))

        """Draw sprites"""
        draw_sprite(niddle, niddle_sprite, screen)
        draw_sprite(ether, ether_sprite, screen)
        draw_sprite(tube, tube_sprite, screen)

        """Draw guardian_sprite"""
        draw_sprite(guardian, guardian_sprite, screen)

        """Draw the maze"""
        maze.draw_maze(screen)

        """Draw the counter sprite"""
        screen.blit(counters[macgyver.inventory], (540, 0))

        """Modifying MacGyver position with inputs"""
        macgyver.movement(maze.struct)

        """Draw MacGyver"""
        draw_sprite(macgyver, macgyver_sprite, screen)

        """Check if he's on an item, if so, add 1 to inventory"""
        for item in items:
            if macgyver.position == item.position:
                macgyver.inventory = macgyver.get_object(item)

        """Check if MacGyver's in front of the guardian"""
        finished = macgyver.check_guardian(guardian)

        """Check if he fills all conditions and if he wins"""
        if finished:
            win = macgyver.win_lose(guardian)
            win_sprite(screen, win)
            keep_going = False
            """Display loosing or winning sprite"""
            pg.display.flip()
            sleep(2)

        pg.display.flip()

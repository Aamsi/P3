from random import randrange
from time import sleep

import pygame as pg


class Character:
    """Character :
       - MacGyver (position and inventory)
       - Guardian (position and inventory = 0)"""

    """Three attributes: position_x, position_y and inventory"""
    def __init__(self, position_x, position_y, inventory):
        self.position = [position_x, position_y]
        self.inventory = inventory

    def movement(self, maze):
        """Modify hero position after asking input"""
        initial_position = [self.position[0], self.position[1]]

        move = input_pg()

        if move == 1:
            self.position[0] += 1

        elif move == 0:
            self.position[0] -= 1

        elif move == 2:
            self.position[1] -= 1

        elif move == 3:
            self.position[1] += 1

        elif move == 4:
            pg.quit()

        self.check_path(maze, initial_position)

    def check_path(self, maze, initial_position):
        """Check if he can move toward the new position"""

        try:
            if maze[self.position[1]][self.position[0]] == 0 or \
               self.position[0] == -1 or self.position[1] == -1:
                self.position = initial_position

        except IndexError:
            self.position = initial_position

    def get_object(self, item):
        """If hero on an item, add 1 to inventory"""

        self.inventory += 1
        item.picked_up()
        return self.inventory

    def check_guardian(self, other):
        """Check if MacGyver's in front of the guardian:"""

        finished = False

        if self.position == other.position:
            finished = True

        return finished

    def win_lose(self, other):
        """Check if MacGyver fills all conditions to win"""

        finished = self.check_guardian(other)

        return finished and self.inventory == 3


class Item:
    """#Item:
       - Niddle
       - Tube
       - Ether
       Each have two attributes: name and position"""

    def __init__(self, nom):
        self.nom = nom
        self.position = []

    def random_pos(self, maze):
        """Generate a random position for item"""

        x = 0
        pos = []
        pos_rand = [0, 0]

        while x < 15:
            y = 1

            while y < 14:
                if maze[y][x] == 1:
                    pos_rand = [x, y]
                    pos.append(pos_rand)
                y += 1
            x += 1

        i = randrange(len(pos))
        coord = pos[i]

        self.position = [coord[0], coord[1]]

    def picked_up(self):
        """Modify item position when picked up"""

        self.position[0] = -100
        self.position[1] = -100


class Maze:
    """Maze has two attributes:
        - Level
        - Its structure """

    def __init__(self, level):
        self.level = level
        self.struct = self.load_maze()

    def load_maze(self):
        """Load the level from the text file"""

        maze = []

        with open(self.level, 'r') as laby:

            for line in laby.readlines():
                line = line.rstrip()

                case_list = []
                for elt in line:
                    case = int(elt)
                    case_list.append(case)

                maze.append(case_list)

        self.laby = maze

        return maze

    def draw_maze(self, tile_wall, ecran):
        """Display the maze, given the level"""

        y = 0
        for line in self.laby:
            x = 0
            for value in line:
                if value == 0:
                    ecran.blit(tile_wall, (x, y))
                x += 40
            y += 40

    def start(self):
        """Find the starting position for MacGyver's position"""

        x = 0
        maze_start = []

        while x < 15:
            y = 0

            while y < 15:
                if self.struct[y][x] == 2:
                    maze_start = [x, y]
                y += 1
            x += 1

        return maze_start

    def end(self):
        """Find the ending position for the Guardian's position"""

        x = 0
        maze_end = []

        while x < 15:
            y = 0

            while y < 15:
                if self.struct[y][x] == 3:
                    maze_end = [x, y]
                y += 1
            x += 1

        return maze_end


def input_pg():
    """Input for the user to move MacGyver or quit
       Used in class method movement()"""
    MOVE_LEFT = 0
    MOVE_RIGHT = 1
    MOVE_UP = 2
    MOVE_DOWN = 3
    QUIT = 4

    move = None

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                move = MOVE_RIGHT

            elif event.key == pg.K_LEFT:
                move = MOVE_LEFT

            elif event.key == pg.K_UP:
                move = MOVE_UP

            elif event.key == pg.K_DOWN:
                move = MOVE_DOWN

            elif event.key == pg.K_ESCAPE:
                move = QUIT

    return move


def load_image(sprite_file):
    """Load every images"""

    sprite_image = pg.image.load(sprite_file).convert_alpha()
    sprite_scaled = pg.transform.scale(sprite_image, (40, 40))

    return sprite_scaled


def draw_sprite(instance, sprite, ecran):
    """Display all instances that interacts with the user"""

    x = instance.position[0] * 40
    y = instance.position[1] * 40

    ecran.blit(sprite, (x, y))


def load_counter_sprite(hero):
    """Counts MacGyver's inventory and load counter sprites"""

    counters_file = ['ressource/compteur_0.png', 'ressource/compteur_1.png',
                     'ressource/compteur_2.png', 'ressource/compteur_3.png']
    counters = []

    for counter_file in counters_file:
        counter = pg.image.load(counter_file).convert_alpha()
        counter_sized = pg.transform.scale(counter, (40, 40))
        counters.append(counter_sized)

    return counters

def win_sprite(screen, win):
    """Display if won or lost"""

    win_loose_files = ['ressource/youWin.png', 'ressource/loose.png']
    win_loose_sprites = []

    for win_loose_file in win_loose_files:
        win_img = pg.image.load(win_loose_file).convert_alpha()
        win_sized = pg.transform.scale(win_img, (400, 300))
        win_loose_sprites.append(win_sized)

    if win:
        screen.blit(win_loose_sprites[0], (100, 200))
    else:
        screen.blit(win_loose_sprites[1], (100, 200))

def main():
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
        tile_wall = load_image('ressource/tile_wall.png')
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
            maze.draw_maze(tile_wall, screen)

            """Draw the counter sprite"""
            screen.blit(counters[macgyver.inventory], (540, 0))

            """Modifying MacGyver position with inputs"""
            macgyver.movement(maze.struct)

            """Draw MacGyver"""
            draw_sprite(macgyver, macgyver_sprite, screen)

            """Check if he's on an item, if so, add 1 to inventory"""
            for item in items:
                if macgyver.position == item.position:
                    macgyver.get_object(item)

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

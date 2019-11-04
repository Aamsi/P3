from random import randrange

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
        self.struct = self.loadmaze()

    def loadmaze(self):
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

    def draw_maze(self, ecran):
        """Display the maze, given the level"""

        wall = pg.image.load('ressource/tile_wall.png').convert_alpha()
        tile_wall = pg.transform.scale(wall, (40, 40))

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


def inventory_counter_sprite(hero, screen):
    """Counts MacGyver's inventory and display number"""

    counters_file = ['ressource/compteur_0.png', 'ressource/compteur_1.png',
                     'ressource/compteur_2.png', 'ressource/compteur_3.png']
    counters = []

    for counter_file in counters_file:
        counter = pg.image.load(counter_file).convert_alpha()
        counter_sized = pg.transform.scale(counter, (40, 40))
        counters.append(counter_sized)

    screen.blit(counters[hero.inventory], (540, 0))


def win_sprite(screen, win):
    """Display if won or lost"""

    win_img = pg.image.load('ressource/youWin.png').convert_alpha()
    win_sized = pg.transform.scale(win_img, (400, 300))

    loose_img = pg.image.load('ressource/loose.png').convert_alpha()
    loose_sized = pg.transform.scale(loose_img, (400, 300))

    if win:
        screen.blit(win_sized, (100, 200))
    else:
        screen.blit(loose_sized, (100, 200))

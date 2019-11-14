from random import randrange
from time import sleep

import pygame as pg

MOVE_LEFT = 0
MOVE_RIGHT = 1
MOVE_UP = 2
MOVE_DOWN = 3
QUIT = 4


class Character:
    """Character :
       - MacGyver (position and inventory=0)
       - Guardian (position and inventory=0)"""

    def __init__(self, position_x, position_y, inventory=0):
        self.position = [position_x, position_y]
        self.inventory = inventory

    def movement(self, maze, move):
        """Modify hero position after asking input"""
        initial_position = [self.position[0], self.position[1]]

        if move == MOVE_RIGHT:
            self.position[0] += 1

        elif move == MOVE_LEFT:
            self.position[0] -= 1

        elif move == MOVE_UP:
            self.position[1] -= 1

        elif move == MOVE_DOWN:
            self.position[1] += 1

        elif move == QUIT:
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

    def check_object(self, items):
        """If hero on an item, add 1 to inventory"""
        for item in items:
            if self.position == item.position:
                self.inventory += 1
                item.picked_up()

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

        x_it = 0
        pos = []
        pos_rand = [0, 0]

        while x_it < 15:
            y_it = 1

            while y_it < 14:
                if maze[y_it][x_it] == 1:
                    pos_rand = [x_it, y_it]
                    pos.append(pos_rand)
                y_it += 1
            x_it += 1

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
        self.start_position = self.start()
        self.end_position = self.end()

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

        y_it = 0
        for line in self.laby:
            x_it = 0
            for value in line:
                if value == 0:
                    ecran.blit(tile_wall, (x_it, y_it))
                x_it += 40
            y_it += 40

    def start(self):
        """Find the starting position for MacGyver's position"""

        x_it = 0
        maze_start = []

        while x_it < 15:
            y_it = 0

            while y_it < 15:
                if self.struct[y_it][x_it] == 2:
                    maze_start = [x_it, y_it]
                y_it += 1
            x_it += 1

        return maze_start

    def end(self):
        """Find the ending position for the Guardian's position"""

        x_it = 0
        maze_end = []

        while x_it < 15:
            y_it = 0

            while y_it < 15:
                if self.struct[y_it][x_it] == 3:
                    maze_end = [x_it, y_it]
                y_it += 1
            x_it += 1

        return maze_end


class PygameTool:
    """Every tool used with pygame"""

    def __init__(self):
        pg.init()

        self.tile_wall = None
        self.macgyver_sprite = None
        self.guardian_sprite = None
        self.niddle_sprite = None
        self.ether_sprite = None
        self.tube_sprite = None
        self.counters = None

    def blit(self, sprite, screen):
        """Blit the screen"""
        screen.blit(sprite, (540, 0))

    def flip(self):
        """Update the screen"""
        pg.display.flip()

    def input_pg(self):
        """Input for the user to move MacGyver or quit
        Used in class method movement()"""
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

    def load_image(self, sprite_file):
        """Load every images"""

        sprite_image = pg.image.load(sprite_file).convert_alpha()
        sprite_scaled = pg.transform.scale(sprite_image, (40, 40))

        return sprite_scaled

    def load_all_sprites(self):
        """Load every sprites with load_image()"""

        self.tile_wall = self.load_image('ressource/tile_wall.png')
        self.macgyver_sprite = self.load_image('ressource/MacGyver.png')
        self.guardian_sprite = self.load_image('ressource/Gardien.png')
        self.niddle_sprite = self.load_image('ressource/aiguille.png')
        self.ether_sprite = self.load_image('ressource/ether.png')
        self.tube_sprite = self.load_image('ressource/tube_plastique.png')
        self.counters = self.load_counter_sprite()

    def draw_sprite(self, instance, sprite, screen):
        """Display all instances that interacts with the user"""

        x_pos = instance.position[0] * 40
        y_pos = instance.position[1] * 40

        screen.blit(sprite, (x_pos, y_pos))

    def load_counter_sprite(self):
        """Counts MacGyver's inventory and load counter sprites"""

        counter_file = ['ressource/compteur_0.png', 'ressource/compteur_1.png',
                        'ressource/compteur_2.png', 'ressource/compteur_3.png']
        counters = []

        for counter_file in counter_file:
            counter = pg.image.load(counter_file).convert_alpha()
            counter_sized = pg.transform.scale(counter, (40, 40))
            counters.append(counter_sized)

        return counters

    def win_sprite(self, win, screen):
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


class GameMaze:
    """Contains every method used to run the game"""

    def __init__(self):
        self.maze = None
        self.macgyver = None
        self.guardian = None
        self.niddle = None
        self.tube = None
        self.ether = None
        self.items = None
        self.screen = None
        self.pg_tool = PygameTool()
        self.finished = None
        self.win = None

    def init_maze(self):
        """Initialize the maze"""

        self.maze = Maze('level0.txt')

    def init_characters(self):
        """Initialize characters"""

        self.macgyver = Character(self.maze.start_position[0],
                                  self.maze.start_position[1])
        self.guardian = Character(self.maze.end_position[0],
                                  self.maze.end_position[1])

    def init_items(self):
        """Initialize items"""

        self.niddle = Item("Aiguille")
        self.niddle.random_pos(self.maze.struct)
        self.tube = Item("Tube en plastique")
        self.tube.random_pos(self.maze.struct)
        self.ether = Item("Ether")
        self.ether.random_pos(self.maze.struct)

        self.items = [self.niddle, self.tube, self.ether]

    def init_pg(self):
        """Initialize pygame"""

        pg.init()
        self.screen = pg.display.set_mode((600, 600), pg.RESIZABLE)
        pg.display.set_caption("THE MAZE")

    def draw_all_sprites(self):
        """Draw every sprites"""
        pg.draw.rect(self.screen, (0, 0, 0), (0, 0, 600, 600))

        self.pg_tool.load_all_sprites()

        self.pg_tool.draw_sprite(self.niddle,
                                 self.pg_tool.niddle_sprite, self.screen)
        self.pg_tool.draw_sprite(self.ether,
                                 self.pg_tool.ether_sprite, self.screen)
        self.pg_tool.draw_sprite(self.tube,
                                 self.pg_tool.tube_sprite, self.screen)
        self.pg_tool.draw_sprite(self.guardian,
                                 self.pg_tool.guardian_sprite, self.screen)
        self.pg_tool.draw_sprite(self.macgyver, self.pg_tool.macgyver_sprite,
                                 self.screen)

        self.maze.draw_maze(self.pg_tool.tile_wall, self.screen)

        self.pg_tool.blit(self.pg_tool.counters[self.macgyver.inventory],
                          self.screen)

    def mg_movement(self):
        """MacGyver movement and draw the MacGyver's sprite"""

        self.macgyver.movement(self.maze.struct, self.pg_tool.input_pg())

    def finish(self):
        """Check if the game is finished, and if it's won or lost"""

        self.finished = self.macgyver.check_guardian(self.guardian)

        if self.finished:
            self.win = self.macgyver.win_lose(self.guardian)
            self.pg_tool.win_sprite(self.win, self.screen)
            self.pg_tool.flip()
            sleep(2)

    def main_loop(self):
        """Main loop to run the game"""

        self.finished = False
        while not self.finished:
            self.mg_movement()
            self.draw_all_sprites()
            self.macgyver.check_object(self.items)
            self.finished = self.macgyver.check_guardian(self.guardian)
            self.finish()
            self.pg_tool.flip()

    def is_won(self):
        """Return if MacGyver wins or looses"""

        return self.win

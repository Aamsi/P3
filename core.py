from random import randrange

import pygame as pg

class Character:
    """Character : 
       - MacGyver (position and inventory)
       - Guardian (position and inventory = 0)"""
    
    """Three attributes: position_x, position_y and inventory"""
    def __init__(self, position_x, position_y, inventory):
        self.position_x = position_x
        self.position_y = position_y
        self.inventory = inventory
    
    def movement(self):
        """Modify hero position after asking input"""

        position = [self.position_x, self.position_y]

        move = input_pg()
        
        if move == 'move right':
            self.position_x += 1
            position[0] = self.position_x

        elif move == 'move left':
            self.position_x -= 1
            position[0] = self.position_x
            
        elif move == 'move up':
            self.position_y -= 1
            position[1] = self.position_y

        elif move == 'move down':
            self.position_y += 1
            position[1] = self.position_y
        
        elif move == 'quit':
            pg.quit()

        return position
    
    def path(self, maze, initial_position):
        """Check if he can move toward the new position"""

        try:
            if maze[self.position_y][self.position_x] == 0 or self.position_x == -1 or self.position_y == -1:
                self.position_x = initial_position[0]
                self.position_y = initial_position[1]

        except IndexError:
            self.position_x = initial_position[0]
            self.position_y = initial_position[1]

    def get_object(self, item):
        """If hero on an item, add 1 to inventory"""

        self.inventory += 1
        item.picked_up()
        return self.inventory
    
    def check_guardian(self, other):
        """Check if MacGyver's in front of the guardian:"""

        finished = False
        x_finished = self.check_x_position(other)
        y_finished = self.check_y_position(other)

        if x_finished and y_finished:
            finished = True
        else:
            finished = False

        return finished

    def win_lose(self, other):
        """Check if MacGyver fills all conditions to win"""

        finished = self.check_guardian(other)
        inventory = self.inventory
    
        win = False
        if finished and inventory == 3:
            win = True
        elif finished and inventory != 3:
            win = False

        return win
    
    def check_x_position(self, other):
        """Check x position"""

        x_finished = False

        if self.position_x == other.position_x:
            x_finished = True
        else:
            x_finished = False
        
        return x_finished
    
    def check_y_position(self, other):
        """Check y position"""

        y_finished = False

        if self.position_y == other.position_y:
            y_finished = True
        else:
            y_finished = False
        
        return y_finished

class Item:
    """#Item:
       - Niddle
       - Tube
       - Ether
       Each have two attributes: name and position"""

    def __init__(self, nom, position=[]):
        self.nom = nom
        self.position = position
        self.position_x = position[0]
        self.position_y = position[1]
    
    def picked_up(self):
        """Modify item position when picked up"""

        self.position_x = -100
        self.position_y = -100
        self.position = [-100, -100]

class Maze:

    def __init__(self, level):
        self.level = level
        self.laby = []
    
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
    
    def maze_interface(self, ecran):
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
    
    def random_pos(self):
        """Generate a random position for item"""

        x = 0
        pos = []
        pos_rand = [0, 0]

        while x < 15:
            y = 1

            while y < 14:
                if self.laby[y][x] == 1:
                    pos_rand = [x, y]
                    pos.append(pos_rand)
                y += 1
            x += 1

        i = randrange(len(pos))
        coord = pos[i]

        return coord


def input_pg():
    """Input for the user to move MacGyver or quit
       Used in class method movement()"""

    move = None

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                move = 'move right'

            elif event.key == pg.K_a:
                move = 'move left'
                
            elif event.key == pg.K_w:
                move = 'move up'
                
            elif event.key == pg.K_s:
                move = 'move down'

            elif event.key == pg.K_ESCAPE:
                move = 'quit'
    
    return move

def sprite_interaction(sprite, sprite_file, ecran):
    """Display all objects that interacts with the user"""

    sprite_image = pg.image.load(sprite_file).convert_alpha()
    sprite_sized = pg.transform.scale(sprite_image, (40, 40))

    x = sprite.position_x * 40
    y = sprite.position_y * 40

    ecran.blit(sprite_sized, (x, y))

def inventory_counter_sprite(hero, screen):
    """Counts MacGyver's inventory and display number"""

    counter_0 = pg.image.load('ressource/compteur_0.png').convert_alpha()
    counter0_sized = pg.transform.scale(counter_0, (40, 40))

    counter_1 = pg.image.load('ressource/compteur_1.png').convert_alpha()
    counter1_sized = pg.transform.scale(counter_1, (40, 40))

    counter_2 = pg.image.load('ressource/compteur_2.png').convert_alpha()
    counter2_sized = pg.transform.scale(counter_2, (40, 40))

    counter_3 = pg.image.load('ressource/compteur_3.png').convert_alpha()
    counter3_sized = pg.transform.scale(counter_3, (40, 40))

    if hero.inventory == 0:
        screen.blit(counter0_sized, (540, 0))
    elif hero.inventory == 1:
        screen.blit(counter1_sized, (540, 0))
    elif hero.inventory == 2:
        screen.blit(counter2_sized, (540, 0))
    elif hero.inventory == 3:
        screen.blit(counter3_sized, (540, 0))
    
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
    

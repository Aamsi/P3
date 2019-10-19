from random import randrange

import pygame as pg

class Character:
    """Character : 
       - MacGyver (position and inventory)
       - Guardian (position and inventory = 0)"""
    
    """Two attributes: position and inventory"""
    def __init__(self, position_x, position_y, inventory):
        self.position_x = position_x
        self.position_y = position_y
        self.inventory = inventory
    
    def movement(self):
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
        try:
            if maze[self.position_y][self.position_x] == 0 or self.position_x == -1 or self.position_y == -1:
                self.position_x = initial_position[0]
                self.position_y = initial_position[1]

        except IndexError:
            self.position_x = initial_position[0]
            self.position_y = initial_position[1]

    def get_object(self, item):
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
        finished = self.check_guardian(other)
        inventory = self.inventory
    
        win = False
        if finished and inventory == 3:
            win = True
            print("Vous avez gagné!")
        elif finished and inventory != 3:
            win = False
            print("Vous n'avez pas assez d'objets pour endormir le guardien!")

        return win
    
    def check_x_position(self, other):
        x_finished = False

        if self.position_x == other.position_x:
            x_finished = True
        else:
            x_finished = False
        
        return x_finished
    
    def check_y_position(self, other):
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
       Each have one attribute: position"""

    def __init__(self, nom, position=[]):
        self.nom = nom
        self.position = position
        self.position_x = position[0]
        self.position_y = position[1]
    
    def picked_up(self):
        self.position_x = -100
        self.position_y = -100
        self.position = [-100, -100]

class Maze:

    def __init__(self, level):
        self.level = level
        self.laby = []
    
    def loadmaze(self):
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
        x = 0
        pos = []
        pos_rand = [0, 0]

        while x < 15:
            y = 0

            while y < 15:
                if self.laby[y][x] == 1:
                    pos_rand = [x, y]
                    pos.append(pos_rand)
                y += 1
            x += 1

        i = randrange(len(pos))
        coord = pos[i]

        return coord



def input_pg():
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

def sprite_print(sprite, sprite_file, ecran):

    sprite_image = pg.image.load(sprite_file).convert_alpha()
    sprite_pict = pg.transform.scale(sprite_image, (40, 40))

    x = sprite.position_x * 40
    y = sprite.position_y * 40

    ecran.blit(sprite_pict, (x, y))

def inventory_counter(hero, screen):
    counter_0 = pg.image.load('ressource/compteur_0.png').convert_alpha()
    counter_pict0 = pg.transform.scale(counter_0, (40, 40))

    counter_1 = pg.image.load('ressource/compteur_1.png').convert_alpha()
    counter_pict1 = pg.transform.scale(counter_1, (40, 40))

    counter_2 = pg.image.load('ressource/compteur_2.png').convert_alpha()
    counter_pict2 = pg.transform.scale(counter_2, (40, 40))

    counter_3 = pg.image.load('ressource/compteur_3.png').convert_alpha()
    counter_pict3 = pg.transform.scale(counter_3, (40, 40))

    if hero.inventory == 0:
        screen.blit(counter_pict0, (540, 0))
    elif hero.inventory == 1:
        screen.blit(counter_pict1, (540, 0))
    elif hero.inventory == 2:
        screen.blit(counter_pict2, (540, 0))
    elif hero.inventory == 3:
        screen.blit(counter_pict3, (540, 0))
    
def win_sprite(screen, win):
    win_img = pg.image.load('ressource/youWin.png').convert_alpha()
    win_sized = pg.transform.scale(win_img, (400, 300))

    loose_img = pg.image.load('ressource/loose.png').convert_alpha()
    loose_sized = pg.transform.scale(loose_img, (400, 300))

    if win:
        screen.blit(win_sized, (100, 200))
    else:
        screen.blit(loose_sized, (100, 200))

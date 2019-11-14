from core import GameMaze


def main():
    """Main function to call to run the game"""

    win = False
    while not win:
        game_maze = GameMaze()

        game_maze.init_maze()
        game_maze.init_characters()
        game_maze.init_items()

        game_maze.pg_init()

        finished = False
        while not finished:
            game_maze.main_loop()

            finished = game_maze.is_finished()

            win = game_maze.is_won()


if __name__ == '__main__':
    main()

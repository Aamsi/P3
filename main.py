from core import GameMaze


def main():
    """Main function to call to run the game"""
    game_maze = GameMaze()

    game_maze.init_maze()
    game_maze.init_characters()
    game_maze.init_items()
    game_maze.init_pg()

    game_maze.main_loop()

    if not game_maze.is_won():
        main()


if __name__ == '__main__':
    main()

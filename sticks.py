"""Create a version of the Game of Sticks where human and
AI players can play against each other.

In the Game of Sticks there is a heap of sticks on a board.
On their turn, each player picks up 1 to 3 sticks. The one
who has to pick the final stick will be the loser."""

def prompt_count():
    """Prompts the player for the number of sticks to begin the game"""
    while True:
        try:
            count = int(input("How many sticks are there on the table initially (10-100)?  "))
            if count < 10 or count > 100:
                count/0
            break
        except:
            print("Please enter an integer between 10 and 100")
            continue
    return count


def prompt_human_count():
    """Prompts the user for the number of human players (0-2)"""
    pass


def turn(count):
    """Prompts the player for the number of sticks to pick up"""
    pass


def main():
    print("Welcome to the Game of Sticks!")
    count = prompt_count()
    turn_alt = 1

#    while count < 0:



if __name__ == '__main__':
    main()

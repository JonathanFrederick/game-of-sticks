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
    while True:
        try:
            humans = int(input("Please input the number of human players (0-2)"))
            if humans < 0 or humans > 2:
                humans/0
            break
        except:
            print("Please enter an integer between 0 and 2")
            continue
    return humans

def get_players(player1 = {}, player2={}):
    pass


def prompt_name(humans):
    """Prompts for player names or returns a dictionary for an AI"""


    return name


def turn(count, player):
    """Prompts the player for the number of sticks to pick up"""
    pass


def main():
    print("Welcome to the Game of Sticks!")
    count = prompt_count()
    turn_alt = 1
    print(prompt_human_count())
#    player1, player2 = prompt_name()
    while count < 0:
        if turn_alt > 0:
            turn(count, player1)



if __name__ == '__main__':
    main()

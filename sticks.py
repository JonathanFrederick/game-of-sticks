"""Create a version of the Game of Sticks where human and
AI players can play against each other.

In the Game of Sticks there is a heap of sticks on a board.
On their turn, each player picks up 1 to 3 sticks. The one
who has to pick the final stick will be the loser."""
def get_int(low, high, prompt):
    """Prompts the player for an integer within a range"""
    while True:
        try:
            integer = int(input(prompt))
            if integer < low or integer > high:
                integer/0
            break
        except:
            print("Please enter an integer between", low, "and", high)
            continue
    return integer


def prompt_count():
    """Prompts the player for the number of sticks to begin the game"""
    return get_int(10, 100, "How many sticks are there on the table initially (10-100)?  ")


def prompt_human_count():
    """Prompts the user for the number of human players (0-2)"""
    return get_int(0, 2, "Please input the number of human players (0-2)")


def prompt_choice(player):
    return get_int(1, 2, player+": How many sticks do you take (1-3)?  ")


def get_players(humans):
    """Prompts for player names or returns a dictionary for an AI"""
    players = []
    ai_count = 1
    while humans > 0:
        players.append(input("Please enter a player name:  "))
        humans -= 1
    while len(players) < 2:
        players.append({"A. I. - " + str(ai_count):{}})
        ai_count += 1
    return players[0], players[1]


def turn(count, player):
    """Prompts the player for the number of sticks to pick up"""
    choice = prompt_choice(player)
    return count, player()


def main():
    print("Welcome to the Game of Sticks!")
    count = prompt_count()
    turn_alt = 1
    player_1, player_2 = get_players(prompt_human_count())
    while count < 0:
        if turn_alt > 0:
            turn, player1 = turn(count, player1)
        else:
            turn, player2 = turn(count, player2)
        turn_alt * -1


if __name__ == '__main__':
    main()

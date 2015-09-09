"""Create a version of the Game of Sticks where human and
AI players can play against each other.

In the Game of Sticks there is a heap of sticks on a board.
On their turn, each player picks up 1 to 3 sticks. The one
who has to pick the final stick will be the loser."""
import random
import sys

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

def set_dict_range(count, ai_dict):
    """Sets default dict with (1,2,3) for range if not defined"""
    for i in range(1, count+1):
        if i not in ai_dict:
            ai_dict[i] = [1, 2 ,3]
    return ai_dict

def reset_dict(ai_dict):
    """Checks each entry in dict for 1, 2, and 3"""
    for hat in ai_dict:
        for choice in (1, 2, 3):
            if choice not in ai_dict[hat]:
                ai_dict[hat].append(choice)
    return ai_dict

def add_dict(player, ai_dict):
    """Adds choices back to dict for winning AI"""
    for choice in player[1]:
        ai_dict[choice[0]].append(choice[1])
    return ai_dict

def subtract_dict(player, ai_dict):
    """Subtracts choices from dict for losing AI"""
    for choice in player[1]:
        ai_dict[choice[0]].remove(choice[1])
    return ai_dict

def update_dict(winner, loser, ai_dict):
    return add_dict(winner, subtract_dict(loser, ai_dict))

def ai_choice(count, player, ai_dict):
    """Chooses a random answer from ai_dict and records it in player's list"""
    choice = random.choice(ai_dict[count])
    player[1].append([count, choice])
    return player, choice

def prompt_count():
    """Prompts the player for the number of sticks to begin the game"""
    return get_int(10, 100, "How many sticks are there on the table initially (10-100)?  ")


def prompt_human_count():
    """Prompts the user for the number of human players (0-2)"""
    return get_int(0, 2, "Please input the number of human players (0-2)")


def prompt_choice(count, player, ai_dict):
    """Prompts the user for a number of sticks to pick up"""
    if isinstance(player, list):
        player, choice = ai_choice(count, player, ai_dict)
        #print(len(player[1]-1))
        print("There were " + str(count) + " sticks and " + player[0] + " picked up " + str(player[1][len(player[1])-1][1]))
        return player, choice
    else:
        return player, get_int(1, 3, "There are " + str(count) + " sticks on the board.\n" + player +": How many sticks do you take (1-3)?  ")


def get_players(humans):
    """Prompts for player names or returns a dictionary for an AI"""
    players = []
    ai_count = 0
    ai_names = ('R. Daneel Olivaw', 'R. Giskard Reventlov')
    while humans > 0:
        players.append(input("Please enter a player name:  "))
        humans -= 1
    while len(players) < 2:
        players.append([ai_names[ai_count],[]])
        ai_count += 1
    return players[0], players[1]


def prompt_mode():
    """Prompts for game mode"""
    return get_int(0, 6, """Please select a mode from the following choices:
    0 - Watch a match between two computers
    1 - Play a match against a computer
    2 - Play a match against a fellow human
    3 - Train the computer
    4 - Reset the computer
    5 - View the AI stats
    6 - Exit this game\n>>""")


def print_ai_dict(ai_dict):
    print(ai_dict)
    for key in range(1, len(ai_dict)+1):
          print(key, "-", ai_dict[key])


def train_ai(ai_dict):
    num_matches = get_int(10, 1000, "Between 10 and 1000, how many matches would you like to run?  ")
    num_sticks = get_int(10, 100, "Between 10 and 100, how many sticks should be at the beginning of these matches?  ")
    while num_matches > 0:
        turn_alt = 1
        count = num_sticks
        ai1 = []
        ai2 = []
        ai_dict = set_dict_range(num_sticks, ai_dict)
        while count > 0:
            if turn_alt > 0:
                ai1.append([count, random.choice(ai_dict[count])])
                count -= ai1[len(ai1)-1][1]
            else:
                ai2.append([count, random.choice(ai_dict[count])])
                count -= ai2[len(ai2)-1][1]
            turn_alt = turn_alt*-1
        if turn_alt > 0:
            add_dict([[],ai1], ai_dict)
            subtract_dict([[],ai2], ai_dict)
        else:
            add_dict([[],ai2], ai_dict)
            subtract_dict([[],ai1], ai_dict)
        reset_dict(ai_dict)
        print("Match", num_matches, "complete")
        num_matches -= 1
    return ai_dict





def turn(count, player, ai_dict):
    """Prompts the player for the number of sticks to pick up"""
    player, choice = prompt_choice(count, player, ai_dict)
    return count - choice, player


def main():
    print("Welcome to the Game of Sticks!")
    ai_dict = {1:[1,2,3], 2:[1,2,3]}
    mode = 0
    while True:
        mode = prompt_mode()
        if mode == 6:
            sys.exit()
        elif mode == 5:
            print_ai_dict(ai_dict)
        elif mode == 4:
            ai_dict == {}
        elif mode == 3:
            ai_dict = train_ai(ai_dict)
        else:
            count = prompt_count()
            turn_alt = 1
            player_1, player_2 = get_players(mode)
            ai_dict = set_dict_range(count, ai_dict)
            while count > 0:
                if turn_alt > 0:
                    count, player_1 = turn(count, player_1, ai_dict)
                else:
                    count, player_2 = turn(count, player_2, ai_dict)
                turn_alt = turn_alt * -1
            if turn_alt > 0:
                if isinstance(player_1, list):
                    add_dict(player_1, ai_dict)
                    print(player_1[0], "wins the game!")
                else:
                    print(player_1, "wins the game!")
                if isinstance(player_2, list):
                    subtract_dict(player_2, ai_dict)
            else:
                if isinstance(player_2, list):
                    add_dict(player_2, ai_dict)
                    print(player_2[0], "wins the game!")
                else:
                    print(player_2, "wins the game!")
                if isinstance(player_1, list):
                    subtract_dict(player_1, ai_dict)


if __name__ == '__main__':
    main()

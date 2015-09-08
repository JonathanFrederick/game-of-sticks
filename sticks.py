"""Create a version of the Game of Sticks where human and
AI players can play against each other.

In the Game of Sticks there is a heap of sticks on a board.
On their turn, each player picks up 1 to 3 sticks. The one
who has to pick the final stick will be the loser."""

def get_count():
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


def main():
    print("Welcome to the Game of Sticks!")
    get_count()

if __name__ == '__main__':
    main()

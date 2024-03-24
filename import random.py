import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        user_input = input("Press 'Enter' to roll the dice or type 'quit' to exit: ")
        if user_input.lower() == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("You rolled a", roll_dice())

if __name__ == "__main__":
    main()


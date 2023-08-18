# ------------------------------------------
# number guessing game => python
# ------------------------------------------

# import random module
import random


# welcome message and instructions for games
print('-'*40)
print("Welcome to the number guessing game!")
print("type exit or q to quit the game ") 
print('-'*40,'\n')


# the main function for the game
def main():
    # define a variable
    number_random = random.randint(1, 10)

    input_user = int(input("Guess a number between 1 and 10: "))

    # while loop for the game
    while input_user != number_random:

        # first condition for the game
        if input_user > number_random:
            print("Too high, try again!")
            input_user = int(input("Guess a number between 1 and 10: "))

        
        # second condition for the game
        elif input_user < number_random:
            print("Too low, try again!")
            input_user = int(input("Guess a number between 1 and 10: "))

    #  third condition for the game
    if input_user == number_random:
        print('-'*40)
        print("You guessed it! You won! \n")
        main()

    # exit the game
    elif input_user == 'exit' or input_user == 'q':
        print("Thanks for playing! See you next time!")
        exit()


# call the main function
main()
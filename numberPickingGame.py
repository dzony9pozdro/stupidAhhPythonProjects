import random
playing_again = "y"
while playing_again == "y":

    tries = 0
    # prompt the user for a range of integers 0 - userDefinedRange.
    user_defined_range = int(input('input the upper limit of the range you want to play in: '))

    # generate a random number within that range of integers.
    winning_number = random.randint(0, user_defined_range)
    # prompt the user for their guess
    while True:

        try: 
            user_guess = int(input(f'input a number in the range of 0 to {user_defined_range} inclusive: '))
            break
        except ValueError:
            user_guess = print(f'please input a number 0 through {user_defined_range} inclusive: ')
    # check if the userGuess is winning, below the target, above the target, or outside of the definedd range
    while user_guess != winning_number:
        tries+=1
        if not (0 <= user_guess <= user_defined_range):
            user_guess = int(input(f'inputted number was outside of the defined range: 0 through {user_defined_range}, try again: '))
        elif user_guess > winning_number:
            user_guess = int(input(f'tries: {tries}  {user_guess} is too high! try again:'))
        elif user_guess < winning_number:
            user_guess = int(input(f'tries: {tries}  {user_guess} is too low! try again:'))
    # determine if the player wants to play again, run the gameLoop again, or exit the game.
    playing_again = input(f'congrats {user_guess} is the correct number, you got it in {tries} tries wanna play again (y/n: )').lower()

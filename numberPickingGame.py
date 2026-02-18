import random
def generate():
    global userDefinedRange
    userDefinedRange =int(input('how many numbers do you want to pick out of?: '))
    global winningNumber
    winningNumber = round(userDefinedRange*random.random())
    # print(winningNumber)
def guess():
    global  userGuess
    userGuess = int(input(f'input your guess in the range of 0 and {int(userDefinedRange)}: '))
def check():
    global playingAgain

    if userGuess == winningNumber:
        playingAgain =  input('congrats, wanna play again? (y/n): ')
    else: playingAgain = input('loser! wanna play again? (y/n): ')
    playingAgain.lower
    match playingAgain:
        case "y":
            gameLoop()
        case "n":
            print('gg ez bye')

def gameLoop():
    generate()
    guess()
    check()
gameLoop()

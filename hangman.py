import random

words = [
    "python", "jungle", "castle", "bridge", "frozen", "planet", "magnet",
    "cactus", "helmet", "bronze", "oyster", "goblin", "sphinx", "turnip",
    "walrus", "fiddle", "gravel", "kennel", "muffin", "noodle", "parrot",
    "quartz", "rabbit", "saddle", "tangle", "umbrella", "velvet", "weasel",
    "zombie", "anchor", "blight", "cobalt", "dagger", "fabric", "gallop",
    "hamlet", "ignite", "jigsaw", "kitten", "locket", "marble", "napkin",
    "oblong", "pillar", "quirky", "rapids", "shovel", "tundra", "uplift",
    "vortex", "wicket", "xyster", "yarrow", "zipper", "banter", "cinder",
    "dolmen", "emblem", "flagon", "gibbet", "hornet", "instep", "jester",
    "knuckle", "lancer", "muster", "nether", "onward", "plinth", "quiver",
    "rampart", "sickle", "timber", "unfurl", "vanish", "whimsy", "xenon",
    "yonder", "zephyr", "blizzard", "crimson", "dwindle"
]

word = random.choice(words)
guessed: set[str] = set()
tries = 0
max_tries = len(word)*2

while not (set(word).issubset(guessed)) and tries<max_tries:
    if tries != 0:
        print(f'guesses: {''.join(guessed)}')

    guess = input('input your guess: ')
    while guess == ' ' or guess == '' or len(guess)>1 or guess in guessed:
        if guess == ' ' or guess == '':
            guess = input("input your guess: ")
        elif len(guess)>1:
            guess = input(f"input 1 letter at a time:")
        elif guess in guessed:
            guess = input(f"you've already guessed {guess}, don't waste a try: ")

    tries+=1
    guessed.add(guess) 

    for letter in word:
        if letter in guessed:
            print(f'{letter}', end=' ')
        else: print(f'_', end = ' ')
    print(f'tries: ({tries} / {max_tries})')
    print(' ')


if set(word).issubset(guessed):
   print('you win! ')
else:
    print(f'you lose, the word was {word}')

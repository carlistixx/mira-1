
import random
import sys


the_cat =  (
    " /\_/\\\n"
    "( o o )\n"
    "==_Y_==\n"
    "  `-'\n"
)

print("Guess which number I am thinking of. You have three chances!")
print("if you get the answer wrong you get a clue")
    
answer = random.randint(1, 10)


def give_clue(guess, answer):
    if i < 2 and int(guess) > answer:
        print("Your guess was too high, dummy. Try lower!")
    else:
        print("Your answer was too low, idiot. Try higher!")


for i in range(3):

    guess = input("Enter your guess: ")
    if int(guess) == answer:
        print("You got the right answer, you get a cat sticker")
        print(the_cat)
        sys.exit(0)
    else:
        print("You got the wrong answer, you lost 5 points. Try again.")
        if i < 2:
            give_clue(guess, answer)
        

print("The answer was %d, better luck next time!" % answer)

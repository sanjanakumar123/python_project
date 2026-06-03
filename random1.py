import random
playing = True
number = str(random.randint(0.9))
print("I will generate a number from 0 to 9, and you have to guess the digit one at a time.")
print("The game ends when you get one hero!")
while playing:
    guess = input("Give me your best guess \n")
    if number == guess:
        print("You win the game")
        print("The number wwas" ,number)
        break
    else:
        print("Your guess is not quite right, try again \n")
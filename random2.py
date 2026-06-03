import random
while True:
    user_actions = input("Enter a choice (rock, paper, or scissors!: )")
    possible_actions = ["rock" , "paper" , "scissors"]
    computer_actions = random.choice(possible_actions)
    print(f"\nYou chose {user_actions}, computer chose {computer_actions}\n")
    if user_actions == computer_actions:
        print(f"both players selected {user_actions}. It is a tie")
    elif user_actions == "rock":
        if computer_actions == "scissors":
            print("rock smashes scissors you win")
        else:
            print("Paper covers rock so you lose")
    elif user_actions == "paper":
        if computer_actions == "rock":
            print("paper covers rock and you win")
        else:
            print("scissors cut paper so you lose")
    elif user_actions == "scissors":
        if computer_actions == "paper":
            print("scissors cut paper you win")
        else:
            print("rock smashes scissors so you lose")
    play_again = input("play again? y or n? ")
    if play_again != "y":
        break
                                           
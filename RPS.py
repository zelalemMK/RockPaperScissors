import random
def rps():
    print("""   Welcome to rock paper scissors""")

    times_play = int(input("How many times do you want to play?"))

    rps = ['rock','paper','scissors']

    user_score = 0
    computer_score = 0
    for i in range(times_play):
        user_choice = input("Rock, Paper or Scissors?").lower()
        computer_choice = random.choice(rps)

        if user_choice == computer_choice:
            print("Tie")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Computer wins")
                computer_score += 1
            else:
                print("User wins")
                user_score += 1
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("Computer wins")
                computer_score += 1
            else:
                print("User wins")
                user_score += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins")
                computer_score += 1
            else:
                print("User wins")
                user_score += 1
    if user_score > computer_score:
        print("YOU WIN THE GAME")
    elif user_score < computer_score:
        print("YOU LOSE THE GAME")
    print("User score: {}".format(user_score))
rps()
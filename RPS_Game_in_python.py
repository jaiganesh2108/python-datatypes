import random

def get_choices():
    player_choice = input("Enter a choise (rock ,paper ,scissor ):")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice,"computer": computer_choice}
    return choices 

def check_win(player,computer):
    print(f"You chose {player} ,computer chose {computer}")
    if player == computer:
        return "Its a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! ,You WIN!"
        else:
            return "Paper covers rock!, You lose!"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! ,You WIN!"
        else:
            return "scissor cuts paper!, You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "paper covers rock! ,You WIN!"
        else:
            return "scissor cuts paper!, You lose!"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)

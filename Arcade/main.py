import random

MIN_GAMES = 1
MAX_GAMES = 2

games = {
    "Rock Paper Scissors": 1,
    "Find the Joker" : 2
    }

def play_rock_paper_scissors():
    print("You have decided to play Rock Paper Scissors!")
    print("The objective of the game is to beat the computer as many times as possible!")
    print("-----------------------------------------------------")
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beat Paper")
    print("You draw if you chooses the same option")
    print("-----------------------------------------------------")
    curr_wins = 0
    curr_loses = 0
    curr_draws = 0
    picks = ["rock", "paper", "scissors"]
    
    while True:
        comp_choice = random.choice(picks)
        player_choice = None
        
        display_msg = "Player chose: [{}]\nComputer chose: [{}]"
        
        while player_choice not in picks and player_choice != 'q':
            player_choice = input("Pick between \'rock\', \'paper\' or \'scissors\' (Type \'q\' to quit): ").lower()
        
        if ((player_choice == 'paper' and comp_choice == 'rock') or
            (player_choice == 'scissors' and comp_choice == 'paper') or
            (player_choice == 'rock' and comp_choice == 'scissors')):
            print(display_msg.format(player_choice, comp_choice))
            print("You won!")
            curr_wins += 1
        elif player_choice == comp_choice:
            print(display_msg.format(player_choice, comp_choice))
            print("You drew!")
            curr_draws += 1
        elif player_choice == 'q':
            break
        else:
            print(display_msg.format(player_choice, comp_choice))
            print("You lost!")
            curr_loses += 1
        print(f"Number of wins: {curr_wins}\nNumber of loses: {curr_loses}\nNumber of draws: {curr_draws}")
    total_games = curr_wins + curr_loses + curr_draws
    if total_games == 0:
        print("Your win rate: 0%")
    else:
        win_rate = round((curr_wins / total_games) * 100, 2)
        print("Your win rate: " + str(win_rate) + "%")
        

def play_joker():
    print("You have decided to play Find the Joker!")
    print("The objective of the game is to find the joker in a standard deck sequence")
    print("The standard deck sequence is 1, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K, A, and the Joker")
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A", "Joker"]
    print("The deck of cards will be shuffled randomly")
    print(f"You pick between 0 -> {len(cards)-1}")
    print("If the number you picked does not contain the Joker, then it will be removed from the deck")
    num_of_lives = 5
    print(f"You have {num_of_lives} lives at the start and 1 life will be deducted if your guess is incorrect\n")
    while True:
        random.shuffle(cards)
        player_choice = input(f"Enter a number between 0 -> {len(cards)-1} (Type q to quit): ")
        if player_choice.isdigit():
            player_choice = int(player_choice)
            if 1 <= player_choice <= len(cards)-1:
                print(f"You chose card {player_choice} which is: {cards[player_choice]}")
                if cards[player_choice] == "Joker":
                    print("You win!")
                    break
                else:
                    print("The card is removed from the deck: ")
                    cards.remove(cards[player_choice])
                    print(cards)
                    num_of_lives -= 1
            else:
                print("Please enter a valid number")
        elif player_choice == 'q':
            break
        else:
            print("Please enter a number")
            
        print(f"You have {num_of_lives} live(s) remaining")
        if num_of_lives == 0:
            print("You couldn't find the Joker. You lost the game.")
            break
    print(f"You left the game with {num_of_lives} live(s) remaining")
            

def select_game(user_choice):
    if user_choice == 1:
        play_rock_paper_scissors()
    elif user_choice == 2:
        play_joker()

def choose_your_game():
    while True:
        choices = " ".join([f"[{game} - ({value})]" for game, value in games.items()])
        user_choice = input(f"Your options include:\n{choices} (the choice must be their respective numbers): ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if MIN_GAMES <= user_choice <= MAX_GAMES:
                return user_choice
            else:
                print(f"Please enter a valid number between {MIN_GAMES} and {MAX_GAMES}.")
        else:
            print("Please enter a number.")

def main():
    print("Welcome to the Arcade!")
    user_choice = choose_your_game()
    select_game(user_choice)

if __name__ == '__main__':
    main()
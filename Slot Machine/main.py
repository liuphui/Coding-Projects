import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 2

ROWS = 3
COLS = 3

symbols_dict = {
    "7": ROWS*3,
    "💎": ROWS*5,
    "🪙": ROWS*10,
    "🍒": ROWS*15,
    "🍋": ROWS*20,
    "🔔": ROWS*30
}

winnings_multipliers = {
    "7": 10,
    "💎": 8,
    "🪙": 6,
    "🍒": 5,
    "🍋": 4,
    "🔔": 3
}

def check_winnings(columns, lines, bet, multipliers):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += multipliers[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i == 0:
                print(f"Line {row}: ", end="")
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row])

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines
    
def get_bet():
    while True:
        bet = input("How much would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a valid bet. Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    num_of_lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * num_of_lines
        if total_bet > balance:
            print("You do not have enough to bet that amount.")
            print(f"Your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {num_of_lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols_dict)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, num_of_lines, bet, winnings_multipliers)
    print(f"You won ${winnings}")
    print(f"You won on line(s):", *winning_lines)
    return winnings - total_bet

def main():
    original_bal = balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}. Your original balance was ${original_bal}")
    if original_bal < balance:
        print(f"You have won ${original_bal - balance}")
    elif original_bal == balance:
        print(f"You broke even!")
    else:
        print(f"You have lost ${original_bal - balance}")
    
main()
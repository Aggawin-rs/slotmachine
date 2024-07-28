#slotmachine
import random
from typing import List, Dict, Tuple

class SlotMachine:
    # Constants
    MAX_LINES = 3
    MAX_BET = 100
    MIN_BET = 1
    ROWS = 3
    COLS = 3
    SYMBOL_COUNT = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8
    }
    SYMBOL_VALUES = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }

    def __init__(self):
        self.balance = 0

    def deposit(self) -> None:
        """Allows user to deposit an amount."""
        while True:
            try:
                amount = int(input("How much do you want to deposit? $"))
                if amount > 0:
                    self.balance = amount
                    break
                else:
                    print("Amount must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_bet(self) -> int:
        """Prompts user to enter a valid bet amount."""
        while True:
            try:
                bet = int(input(f"Enter bet amount (${self.MIN_BET} to ${self.MAX_BET}): "))
                if self.MIN_BET <= bet <= self.MAX_BET:
                    return bet
                else:
                    print(f"Bet must be between ${self.MIN_BET} and ${self.MAX_BET}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_lines(self) -> int:
        """Prompts user to select a number of lines to bet on."""
        while True:
            try:
                lines = int(input(f"Enter number of lines to bet on (1-{self.MAX_LINES}): "))
                if 1 <= lines <= self.MAX_LINES:
                    return lines
                else:
                    print(f"Please enter a number between 1 and {self.MAX_LINES}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_slot_machine_spin(self) -> List[List[str]]:
        """Generates a new slot machine spin."""
        all_symbols = [symbol for symbol, count in self.SYMBOL_COUNT.items() for _ in range(count)]
        columns = [random.sample(all_symbols, self.ROWS) for _ in range(self.COLS)]
        return columns

    def print_slot_machine(self, columns: List[List[str]]) -> None:
        """Prints the slot machine results."""
        for row in range(len(columns[0])):
            print(' | '.join(column[row] for column in columns))

    def check_winnings(self, columns: List[List[str]], lines: int, bet: int) -> Tuple[int, List[int]]:
        """Calculates and returns winnings and winning lines."""
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            if all(column[line] == symbol for column in columns):
                winnings += self.SYMBOL_VALUES[symbol] * bet
                winning_lines.append(line + 1)
        return winnings, winning_lines

    def spin(self) -> int:
        """Executes a spin and returns net result."""
        lines = self.get_lines()
        while True:
            bet = self.get_bet()
            total_bet = bet * lines
            if total_bet > self.balance:
                print(f"Insufficient funds. Your balance is ${self.balance}.")
            else:
                break

        print(f"Your bet: ${bet} on {lines} lines. Total bet: ${total_bet}.")
        columns = self.get_slot_machine_spin()
        self.print_slot_machine(columns)
        winnings, winning_lines = self.check_winnings(columns, lines, bet)
        print(f"You won ${winnings}.")
        if winning_lines:
            print(f"Winning lines: {', '.join(map(str, winning_lines))}.")
        else:
            print("No winning lines.")
        return winnings - total_bet

    def main(self) -> None:
        """Main game loop."""
        self.deposit()
        while True:
            print(f"Current balance: ${self.balance}.")
            if input("Press Enter to spin (q to quit): ").lower() == 'q':
                break
            self.balance += self.spin()
        print(f"You left with ${self.balance}.")

if __name__ == "__main__":
    SlotMachine().main()



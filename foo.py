class Game:
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.can_fly = False

    def start(self):
        print("Welcome to the Adventure Game!")
        print("Your journey begins now...\n")
        self.first_choice()

    def first_choice(self):
        print("You find yourself at a crossroads. Do you want to go left or right?")
        choice = input("Type 'left', 'right', or 'fly': ").strip().lower()
        if choice == 'left':
            self.left_path()
        elif choice == 'right':
            self.right_path()
        elif choice == 'fly':
            self.fly_to_end()
        else:
            print("Invalid choice. Please try again.")
            self.first_choice()

    def left_path(self):
        print("\nYou walk down the left path and encounter a wild animal!")
        print("Do you want to fight or run?")
        choice = input("Type 'fight', 'run', or 'fly': ").strip().lower()
        if choice == 'fight':
            self.fight_animal()
        elif choice == 'run':
            self.run_away()
        elif choice == 'fly':
            self.fly_to_end()
        else:
            print("Invalid choice. Please try again.")
            self.left_path()

    def right_path(self):
        print("\nYou walk down the right path and find a treasure chest!")
        print("Do you want to open it or leave it?")
        choice = input("Type 'open', 'leave', or 'fly': ").strip().lower()
        if choice == 'open':
            self.open_chest()
        elif choice == 'leave':
            self.leave_chest()
        elif choice == 'fly':
            self.fly_to_end()
        else:
            print("Invalid choice. Please try again.")
            self.right_path()

    def fight_animal(self):
        print("\nYou chose to fight the animal.")
        print("You lose 20 health points in the battle, but you defeat the animal!")
        self.health -= 20
        self.check_health()

    def run_away(self):
        print("\nYou chose to run away.")
        print("You safely escape, but you feel a bit cowardly.")
        self.first_choice()

    def open_chest(self):
        print("\nYou open the chest and find a health potion!")
        print("You gain 20 health points.")
        self.health += 20
        self.check_health()

    def leave_chest(self):
        print("\nYou chose to leave the chest untouched.")
        self.first_choice()

    def check_health(self):
        if self.health > 0:
            print(f"\nYour current health is {self.health}.")
            print("Your adventure continues...\n")
            self.first_choice()
        else:
            print("\nYou have no health left. Game over!")
            self.end_game()

    def fly_to_end(self):
        print("\nYou have chosen to fly to the end of the game!")
        self.end_game()

    def end_game(self):
        print("Thank you for playing the Adventure Game!")

if __name__ == "__main__":
    game = Game()
    game.start()


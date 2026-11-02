import random

print("===== STONE PAPER SCISSORS =====")

user_score = 0
computer_score = 0

choices = ["stone", "paper", "scissors"]

while True:

    print("\n1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "4":
        break

    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue

    user = choices[int(user_choice) - 1]
    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a Draw!")

    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):

        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nYour Score:", user_score)
    print("Computer Score:", computer_score)

print("\nFinal Score:")
print("Your Score:", user_score)
print("Computer Score:", computer_score)
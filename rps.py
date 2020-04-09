print("Welcome, let's play some Rock Paper Sissors!")

p1_choice = input("Enter Your choice Player 1: ")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
print("*NO CHEATING*")
p2_choice = input("Enter Your choice Player 2: ")

if p1_choice == p2_choice:
	print("Tie!")
# Choices for if Player 1 enters rock
elif p1_choice == "rock":
	if p2_choice == "sissors":
		print("Player 1 smashes Player 2! Player 1 wins!")
	elif p2_choice == "paper":
		print("Player 2 covers Player 1! Player 2 wins!")
# logic for if player 1 enters paper
elif p1_choice == "paper":
	if p2_choice == "sissors":
		print("Player 2 Cuts through Player 1! Player 2 wins!")
	elif p2_choice == "rock":
		print("Player 1 covers Player 2! Player 1 wins!")
# logic for if player 1 enters sissors
elif p1_choice == "sissors":
	if p2_choice == "rock":
		print("Player 2 smashes Player 1! Player 2 wins!")
	elif p2_choice == "paper":
		print("Player 1 Cuts through Player 2! Player 1 wins!")

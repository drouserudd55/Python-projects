import random

print("Welcome, let's play some Rock Paper Sissors!")

players = input("Are you playing with 1 or 2 players? ")

if players == "1" or players == "one":
	p1_choice = input("Enter Your choice Player: ")
	com_choice = random.randint(1, 3)

	if com_choice == 1:
		com_choice = "rock"
	elif com_choice == 2:
		com_choice = "paper"
	else:
		com_choice = "sissors"

	print("Computer picked " + com_choice)

	if p1_choice == com_choice:
		print("Tie!")
	# Logic for if player enters rock
	elif p1_choice == "rock":
		if com_choice == "sissors":
			print("Player smashes Computer! Player wins!")
		elif com_choice == "paper":
			print("Computer covers Player! Computer wins!")
	# logic for if player enters paper
	elif p1_choice == "paper":
		if com_choice == "sissors":
			print("Computer Cuts through Player! Computer wins!")
		elif com_choice == "rock":
			print("Player covers Computer! Player wins!")
	# logic for if player enters sissors
	elif p1_choice == "sissors":
		if com_choice == "rock":
			print("Computer smashes Player! Computer wins!")
		elif com_choice == "paper":
			print("Player Cuts through Computer! Player wins!")
	else:
		print("You messed up, please enter 'rock' 'paper' or 'sissors' as your selection")


elif players == "2" or players == "two":
	p1_choice = input("Enter Your choice Player 1: ")
	print("*NO CHEATING*\n" * 30)
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
	else:
		print("You messed up, please enter 'rock' 'paper' or 'sissors' as your selection")


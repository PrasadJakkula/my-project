import random
#The introduction and greeting for the user.
print('\n\t\t\tWelcome to the game of\n\n\n\t\t\t "Rock,Paper,Scissor"')
print('\n\n')

#Moves that a person has
moves = ['rock','paper','scissors']

def players_movement():
	#prompt the player to enter their move
	players = input("\nPlease 'Enter' your move.('rock','paper','scissors'):")
	return players
	
def ai_move(players_move):
	#If nor move have been made, randomly choose a move.
	if not players_move:
		return random.choice(moves)
	
	#Find the most common move from the players moves.
	most_common_move = (max(set(players_move),key=players_move.count))
	
	#Choose a counter move based on the players previous moves.
	if most_common_move == 'rock':
		return 'paper'
	elif most_common_move == 'paper':
		return 'scissors'
	elif most_common_move == 'scissors':
		return 'rock'
		
	
players_move = []
		
def winners_decleration():
	while True:
		player = players_movement()#Get the player's move
		ai = ai_move(players_move)#Get the ai's move
		players_move.append(player)#Keep track of the players's moves
		if player in moves:
			print("You choose "+player)
			print("And AI choose "+ai)
			
			#Determine the winner.
			if player == ai:
				print(">>>>>The Match is draw")
			elif player == 'rock' and ai == 'scissors' or player == 'paper' and ai == 'rock' or player == 'scissors' and ai == 'paper':
				print(">>>>>You Win")
			else:
				print(">>>>>Ai Won")
		else:
			print("Please enter.(rock, paper or scissors)")
			
		#Ask if the player wants to play again.
		again = input("Do you want to play another round (yes/no):")
		if again == 'no':
			print("\nThank you for playing the game.")
			break
		
winners_decleration()


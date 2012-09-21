import gp
import random

# def has_winner(board):
# 	if board[0]==1:
# 		return 1
# 	elif board[-1]==1:
# 		return 2
# 	else:
# 		return 0

# class Player:
# 	def __init__(self, nmbr):
# 		self.money = 100
# 		self.nmbr=nmbr

# 	def evaluate(self, a_board):
# 		bid = random.randint(0, self.money)
# 		return bid

# def bidgame(player1, player2):
# 	board = [0, 0, 0, 1, 0, 0, 0]
# 	tiebreak = -1

# 	money = {
# 		"player1":100,
# 		"player2":100
# 	}

# 	moves = 0
# 	while has_winner(board)==0 and moves<100:

# 		player1_bid = player1.evaluate(board)
# 		player2_bid = player2.evaluate(board)

# 		money["player1"] -= player1_bid
# 		money["player2"] -= player2_bid
		
# 		if tiebreak==-1:
# 			if money["player1"] < 0:
# 				return 2
# 			elif money["player2"] < 0:
# 				return 1
# 		else:
# 			if money["player2"] < 0:
# 				return 1
# 			elif money["player1"] < 0:
# 				return 2

# 		prev_S = board.index(1)
# 		board[prev_S] = 0

# 		if player1_bid==player2_bid:
# 			board[prev_S + tiebreak] = 1
# 			tiebreak *= -1
# 		elif player1_bid > player2_bid:
# 			board[prev_S-1] = 1 
# 		else:
# 			board[prev_S+1] = 1

# 		moves += 1

# 	return has_winner(board)

# # player1 = Player(-1)
# # player2 = Player(1)
# # player1 = gp.makerandomtree(4)
# # player2 = gp.makerandomtree(4)

# # tourney_champ = gp.tournament([player1, player2], bidgame)

champ = gp.evolve(10, 50, gp.tournament, maxgen=50, treedepth=10)
print "WINNER IS:"
print champ

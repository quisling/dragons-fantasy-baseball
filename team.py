from player import *

class Team(object):
	"""Tracks a team of 4 players: 2 Hitters 1 SP 1 RP
	"""
	def __init__(self, name, owner, season):
		self.NUM_GAMES = 12
		self.name = name
		self.owner = owner
		self.season = season
		self.players = []
		# Players[0] is Position Player 1
		# Players[1] is Position Player 2
		# Players[2] is Staring Pitcher
		# Players[3] is Relief Pitcher
		for game in range(self.NUM_GAMES):
			self.players.append([[""], [""], [""], [""]])

	def add_player(self, start, end, player, position=0):
		"""If player is pitcher, nothing required.
		
		Otherwise, position=0 is for player one
		position=1 is for player two
		"""
		if player.type == "Relief Pitcher":
			pos = 3
		elif player.type == "Starting Pitcher":
			pos = 2
		else:
			pos = position
		for game in range(start, end):
			self.players[game][pos] = player

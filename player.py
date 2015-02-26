from getstats import *

class Player(object):
	"""Tracks name, type, stats for a single season
	"""
	def __init__(self, name, type, total_games):
		self.name = name
		self.type = type
		self.games = []
		for game in range(total_games):
			self.games.append(get_stats(game, self.name, self.type))

	def get_game_stats(self, game_number):
		return self.games[game_number]

	def get_sum_range(self, begin, end):
		sum = get_empty_stats(self.type)
		for game in range(begin, end):
			sum = sum + self.get_game_stats(game)
		return sum

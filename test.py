from team import *

HIT_WEIGHTS = HitWeightBlock()
SP_WEIGHTS = PitchWeightBlock("SP")
RP_WEIGHTS = PitchWeightBlock("RP")

NUM_GAMES = 12

#print("Hitter Weights:")
#for stat in HIT_WEIGHTS.stats:
#	print(stat, HIT_WEIGHTS.stats[stat])
#print()
#print("Starting Pitcher Weights:")
#for stat in SP_WEIGHTS.stats:
#	print(stat, SP_WEIGHTS.stats[stat])
#print()
#print("Relief Pitcher Weights:")
#for stat in RP_WEIGHTS.stats:
#	print(stat, RP_WEIGHTS.stats[stat])

#team1 = Team("The Dirty Dickpunchers", "Nick", "2014")
#print(team1.name)
#print(team1.owner)
#print(team1.season)
#for game,i in zip(team1.players, range(len(team1.players))):
#	print("%3s: %s %s %s %s" % ((i+1), team1.players[i][0],
#								  team1.players[i][1],
#								  team1.players[i][2],
#								  team1.players[i][3]))
#player1 = Player("SP Richards", "Starting Pitcher", NUM_GAMES)
#player4 = Player("RP Yohey", "Relief Pitcher", NUM_GAMES)
#player12 = Player("PP Marshall", "Position Player", NUM_GAMES)
#player42 = Player("PP Mowen", "Position Player", NUM_GAMES)
#player69 = Player("PP Idzak", "Position Player", NUM_GAMES)
#team1.add_player(0, NUM_GAMES, player1)
#team1.add_player(0, NUM_GAMES, player4)
#team1.add_player(0, NUM_GAMES, player12, 0)
#team1.add_player(0, (NUM_GAMES // 2), player42, 1)
#team1.add_player((NUM_GAMES // 2), NUM_GAMES, player69, 1)
#print()
#for game,i in zip(team1.players, range(len(team1.players))):
#	print("%3s: %s %s %s %s" % ((i+1), (team1.players[i][0]).name,
#								  (team1.players[i][1]).name,
#								  (team1.players[i][2]).name,
#								  (team1.players[i][3]).name))
#print("Nicholas Richards' Stats:")
#for game, i in zip(player1.games, range(len(player1.games))):
#	print("Game #%s:" % (i+1))
#	for stat in game.stats:
#		print(stat, game.stats[stat])
#print("%s's Total Stats:" % player12.name)
total_stat_player1 = player12.get_sum_range(0, NUM_GAMES) * HIT_WEIGHTS
#for stat in total_stat_player1.stats:
#	print(stat, total_stat_player1.stats[stat])
#print()
#print("Total Score: %d" % (total_stat_player1))

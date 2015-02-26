class Stat(object):
	def __init__(self):
		self.stats = {}
	def __add__(self, other):
		

class HitStat(Stat):
	"""Starter stat class for hitters
	
	This starter class for hitters simply initializes the
	hitter stats variables. Will be instantialized within
	static variable for hitter point assignment and individual
	player's by-games stats.
	"""
	def __init__(self, g=0, ab=0, r=0, h=0, b2=0, b3=0, hr=0, rbi=0,
			 tb=0, bb=0, so=0, sb=0, cs=0, hbp=0, sf=0, sh=0, gidp=0, err=0, misc=0):
		"""Takes arguments for stats dict.
		"""

		self.g = g
		self.ab = ab
		self.h = h
		self.tb = tb

		try:
			self.obp = (h + bb + hbp) / (ab + bb + hbp + sf)
		except ZeroDivisionError:
			self.obp = 0.0
		try:
			self.slg = tb / ab
		except ZeroDivisionError:
			self.slg = 0.0
		try:
			self.avg = h / ab
		except ZeroDivisionError:
			self.avg = 0.0
		ops = self.obp + self.slg
		b1 = h - (b2 + b3 + hr)

		self.stats = {
			"R" : r,
			"1B" : b1,
			"2B" : b2,
			"3B" : b3,
			"HR" : hr,
			"RBI" : rbi,
			"BB" : bb,
			"SO" : so,
			"SB" : sb,
			"CS" : cs,
			"HBP" : hbp,
			"SF" : sf,
			"SH" : sh,
			"GIDP" : gidp,
			"ERR" : err,
			"MISC" : misc
			}

	def __add__(self, other):
		g = self.g + other.g
		ab = self.ab + other.ab
		h = self.h + other.h
		tb = self.tb + other.tb
		# new_stat = HitStat()
		# for stat in self.stats:
		#	new_stat.stats[stat] = self.stats[stat] + other.stats[stat]
		r = self.stats["R"] + other.stats["R"]
		b2 = self.stats["2B"] + other.stats["2B"]
		b3 = self.stats["3B"] + other.stats["3B"]
		hr = self.stats["HR"] + other.stats["HR"]
		rbi= self.stats["RBI"] + other.stats["RBI"]
		bb = self.stats["BB"] + other.stats["BB"]
		so = self.stats["SO"] + other.stats["SO"]
		sb = self.stats["SB"] + other.stats["SB"]
		cs = self.stats["CS"] + other.stats["CS"]
		hbp = self.stats["HBP"] + other.stats["HBP"]
		sf = self.stats["SF"] + other.stats["SF"]
		sh = self.stats["SH"] + other.stats["SH"]
		gidp = self.stats["GIDP"] + other.stats["GIDP"]
		err = self.stats["ERR"] + other.stats["ERR"]
		misc = self.stats["MISC"] + other.stats["MISC"]
		
		return HitStat(g, ab, r, h, b2, b3, hr, rbi, tb, bb, so,
							sb, cs, hbp, sf, sh, gidp, err, misc)

	def __mul__(self, other):
		new_stat = HitSolution(
								(self.stats["R"] * other.stats["R"]),
								(self.stats["1B"] * other.stats["1B"]),
								(self.stats["2B"] * other.stats["2B"]),
								(self.stats["3B"] * other.stats["3B"]),
								(self.stats["HR"] * other.stats["HR"]),
								(self.stats["RBI"] * other.stats["RBI"]),
								(self.stats["BB"] * other.stats["BB"]),
								(self.stats["SO"] * other.stats["SO"]),
								(self.stats["SB"] * other.stats["SB"]),
								(self.stats["CS"] * other.stats["CS"]),
								(self.stats["HBP"] * other.stats["HBP"]),
								(self.stats["SF"] * other.stats["SF"]),
								(self.stats["SH"] * other.stats["SH"]),
								(self.stats["GIDP"] * other.stats["GIDP"]),
								(self.stats["ERR"] * other.stats["ERR"]),
								(self.stats["MISC"] * other.stats["MISC"])
							)
		
		return new_stat

class HitMultiplier(HitStat):
	def __init__(self):
		super(HitMultiplier, self).__init__(
			  0, # Games
			  0, # At Bats
			  1, # Runs
			  10,# Hits
			  2, # Doubles
			  3, # Triples
			  4, # Home Runs
			  1, # Runs Batted In
			  0, # Total Bases
			  1, # Walks
			  -1,# Strike Outs
			  1, # Stolen Bases
			  -1,# Caught Stealing
			  1, # Hit By Pitch
			  1, # Sacrifice Flies
			  1, # Sacrifice Hits
			  -1,# Ground Into Double Play
			  -3,# Errors
			  1  # Miscellaneous
			  )
class HitSolution(HitStat):
	def __init__(self, r, b1, b2, b3, hr, rbi, bb, so, sb, cs, hbp,
				 sf, sh, gidp, err, misc):
		self.sum = 0
		self.stats = {
			"R" : r,
			"1B" : b1,
			"2B" : b2,
			"3B" : b3,
			"HR" : hr,
			"RBI" : rbi,
			"BB" : bb,
			"SO" : so,
			"SB" : sb,
			"CS" : cs,
			"HBP" : hbp,
			"SF" : sf,
			"SH" : sh,
			"GIDP" : gidp,
			"ERR" : err,
			"MISC" : misc
			}
		for stat in self.stats:
			self.sum = self.sum + self.stats[stat]
	def __repr__(self):
		return self.sum
	def __int__(self):
		return self.sum
			

class PitchStat(Stat):
	"""Starter stat class for pitchers
	
	This starter class for pitchers simply initializes the
	pitcher stats variables. Will be instantialized within
	static variable for pitcher point assignment and individual
	player's by-games stats.
	"""
	def __init__(self, W=0, L=0, g=0, gs=0, cg=0, sho=0, sv=0,
				 ip=0.0, h=0, r=0, er=0, hr=0, hb=0, bb=0, so=0,
				 hld=0, gf=0, bk=0, wp=0, err=0, misc=0):
		"""Takes arguments for stats dict.
		"""

		self.g = g
		self.gs = gs
		self.sho = sho
		self.h = h
		self.r = r
		self.ur = r - er
		self.hld = hld
		self.gf = gf

		try:
			self.era = 9 * (er / ip)
		except ZeroDivisionError:
			self.era = 0.00
		try:
			self.whip = (bb + h) / ip
		except ZeroDivisionError:
			self.whip = 0.0

		self.stats = {
			"W" : W,
			"L" : L,
			"CG" : cg,
			"SV" : sv,
			"IP" : ip,
			"ER" : er,
			"HR" : hr,
			"HBP" : hb,
			"BB" : bb,
			"SO" : so,
			"BK" : bk,
			"WP" : wp,
			"ERR" : err,
			"MISC" : misc
			}

	def __add__(self, other):
		g =  self.g + other.g
		gs = self.gs + other.gs
		sho = self.sho + other.sho
		h = self.h + other.h
		r = self.r + other.r
		hld = self.hld + other.hld
		gf = self.gf + other.gf
		
		# new_stat = PitchStat()
		# for stat in self.stats:
		#	new_stat.stats[stat] = self.stats[stat] + other.stats[stat]
		
		W = self.stats["W"] + other.stats["W"]
		L = self.stats["L"] + other.stats["L"]
		cg = self.stats["CG"] + other.stats["CG"]
		sv = self.stats["SV"] + other.stats["SV"]
		ip = self.stats["IP"] + other.stats["IP"]
		er = self.stats["ER"] + other.stats["ER"]
		hr = self.stats["HR"] + other.stats["HR"]
		hb = self.stats["HBP"] + other.stats["HBP"]
		bb = self.stats["BB"] + other.stats["BB"]
		so = self.stats["SO"] + other.stats["SO"]
		bk = self.stats["BK"] + other.stats["BK"]
		wp = self.stats["WP"] + other.stats["WP"]
		err = self.stats["ERR"] + other.stats["ERR"]
		misc = self.stats["MISC"] + other.stats["MISC"]
		
		return PitchStat(W, L, g, gs, cg, sho, sv, ip, h, r,
							  er, hr, hb, bb, so, hld, gf, bk, wp,
							  err, misc)

	def __mul__(self, other):
		new_stat = PitchStat()
		
		new_stat.stats["W"] = self.stats["W"] * other.stats["W"]
		new_stat.stats["L"] = self.stats["L"] * other.stats["L"]
		new_stat.stats["CG"] = self.stats["CG"] * other.stats["CG"]
		new_stat.stats["SV"] = self.stats["SV"] * other.stats["SV"]
		new_stat.stats["IP"] = self.stats["IP"] * other.stats["IP"]
		new_stat.stats["ER"] = self.stats["ER"] * other.stats["ER"]
		new_stat.stats["HR"] = self.stats["HR"] * other.stats["HR"]
		new_stat.stats["HBP"] = self.stats["HBP"] * other.stats["HBP"]
		new_stat.stats["BB"] = self.stats["BB"] * other.stats["BB"]
		new_stat.stats["SO"] = self.stats["SO"] * other.stats["SO"]
		new_stat.stats["BK"] = self.stats["BK"] * other.stats["BK"]
		new_stat.stats["WP"] = self.stats["WP"] * other.stats["WP"]
		new_stat.stats["ERR"] = self.stats["ERR"] * other.stats["ERR"]
		new_stat.stats["MISC"] = self.stats["MISC"] * other.stats["MISC"]
		
		return new_stat

class PitchMultiplier(PitchStat):
	def __init__(self, type):
		if type == "SP":
			super(PitchMultiplier, self).__init__(
				  4, # Wins
				  -4,# Losses
				  0, # Games
				  0, # Games Started
				  10,# Complete Games
				  0, # Shutouts
				  3, # Saves
				  1, # Innings Pitched
				  0, # Hits
				  0, # Runs
				  -1,# Earned Runs
				  -1,# Home Runs
				  -1,# Hit By Pitch
				  -0.5,# Walks
				  1, # Strike Outs
				  0, # Holds
				  0, # Games Finished
				  -1,# Balks
				  -1,# Wild Pitches
				  -3,# Errors
				  1  # Miscellaneous
				  )
		elif type == "RP":
			super(PitchMultiplier, self).__init__(
				  4, # Wins
				  -4,# Losses
				  0, # Games
				  0, # Games Started
				  10,# Complete Games
				  0, # Shutouts
				  3, # Saves
				  0.5,# Innings Pitched
				  0, # Hits
				  0, # Runs
				  -1,# Earned Runs
				  -1,# Home Runs
				  -1,# Hit By Pitch
				  -0.5,# Walks
				  1, # Strike Outs
				  0, # Holds
				  0, # Games Finished
				  -1,# Balks
				  -1,# Wild Pitches
				  -3,# Errors
				  1  # Miscellaneous
				  )
		else:
			raise NotImplementedError("No such Pitcher Weight Type")
#!/usr/bin/env python3

##GLOBAL LISTS TO BE USED
neg_keys = []
pos_keys = []
neg_emote_key = []
pos_emote_keys = []
chat1 = []
chat2 = []
caht3 = []
master_chat = []
##SETS UP DICTIONARY WITH TEAM NAMES AND MEMBERS FOR SENTIMENT ANALYSIS
teams = dict()
teams["boston_uprising"] = ["DreamKazper","Snow","Gamsu","NotE","Neko","Avast","STRIKER","Kalios","Mistakes","Kellex"]
teams["dallas_fuel"] = ["HarryHook","aKm","Rascal","OGE","Taimou","Custa","Chipshajen","Mickie","Seagull","cocco","EFFECT"]
teams["la_valiant"] = ["Silkthread","Grimreality","Kariv","Fate","Verbo","Envy","Space","Numlocked","Unkoe","Agilities","Soon"]
teams["ny_excelsior"] = ["Saebyeolbe","Meko","Pine","Janus","Jjonak","Mano","Libero","Ark"]
teams["florida_mayhem"] = ["zappis","Manneten","Sayaplayer","Logix","Zebbosai","CWoosH","TviQ","aWesomeGuy","Zuppeh"]
teams["houston_outlaws"] = [ "Muma","Bani","Clockwork","Mendokusaii","Boink","FCTFCTN","LiNkzr","SPREE","Rawkus","Jake","Coolmatt"]
teams["london_spitfire"] = ["Gesture","birdring","Bdosin","NUS","Hooreg","Fury","HaGoPeun","WooHyaL","Profit","TiZi","Closer"]
teams["la_gladiators"] = ["Asher","Surefour","iRemiix","Fissure","Bischu","Shaz","Hydration","BigGoose"]
teams["philly_fusion"] = ["Joemeister","Boombox","Carpe","Snillo","fragi","Eqo","ShaDowBurn","Neptuno","DayFly","Hotba","Poko","SADO"]
teams["sf_shock"] = ["Moth","dhaK","super","BABYBAY","sinatraa","sleepy","Danteh","Nomy","iddqd","Nevix","Architect"]
teams["seoul_dynasty"] = ["Bunny","Miro","XepheR","gido","Wekeed","Munchkin","ZUNBA","KuKi","tobi","ryujehong","Gambler","FLETA"]
teams["shanghai_dragons"] = ["Geguri","Undead","MG","Roshan","Diya","Freefeel","Xushu","Fiveking","Altering","Ado","Sky","Fearless"]

def load_keywords():
	for line in open("negative.txt"):
		neg_keys.append(line)

	for line in open("positive.txt"):
		pos_keys.append(line)

	for line in open("negativeemotes.txt"):
		neg_emote_keys.append(line)

	for line in open("positiveemotes.txt"):
		pos_emote_keys.append(line)

def load_chats(file1, file2, file3):
	for line in open(file1):
		chat1.append(line)

	for line in open(file2):
		chat2.append(line)

	for line in open(file3):
		chat3.append(line) 
	master_chat.append(chat1)
	master_chat.append(chat2)
	master_chat.append(chat3)

def analyze(team1, team2):
	'''
	takes the messages in split list format for each chat and compares it to sets of keys.
		if the comparison is empty the value of the var will be False
		if comparisons to pos and neg keys return we check that there is a player and team to attach the point to
		if there is then we add of subtract a point toward that teams prediction
	'''
	chat_count = 1
	for chats in master_chat:
		for message in chat:
			split = message.lower().split()
			pos_key_exists = set(split) & set(pos_keys)
			neg_key_exists = set(split) & set(neg_keys)
			pos_emote_exists = set(split) & set(pos_emote_keys)
			neg_emote_exists = set(split) & set(neg_emote_keys)
			team1_player = set(split) & set(teams[team1])
			team2_player = set(split) & set(teams[team2])

			if (bool(pos_key_exists) or bool(pos_emote_keys)) is True and bool(team1_player) is True:
				team1_count += 1

			if (bool(neg_key_exists) or bool(neg_emote_keys)) is True and bool(team1_player) is True:
				team1_count -= 1

			if (bool(pos_key_exists) or bool(pos_emote_keys)) is True and bool(team2_player) is True:
				team2_count += 1

			if (bool(neg_key_exists) or bool(neg_emote_keys)) is True and bool(team2_player) is True:
				team2_count -= 1
			print("For chat file %d: %s score %d, %s score %d " % (chat_count, team1, team1_count, team2, team2_count))
			chat_count += 1


if __name__=="__main__":
	file1 = input("Enter File 1\n")
	file2 = input("Enter File 2\n")
	file3 = input("Enter File 3\n")
	team1 = input("Enter team 1\n")
	team2 = input("Enter team 2\n")
	load_chats(file1, file2, file3)

'''how i think shit will work:
-people watching matches and recording the match chat in intervals
-take the created files and tally the positive and negative for each team for each game at the intervals and make predictions based on that
-we do this for each match in a series.
--use those individual game predictions in order to predict the outcome of the overall series'''

	


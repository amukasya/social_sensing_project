#!/usr/bin/env python3

##SETS UP DICTIONARY WITH TEAM NAMES AND MEMBERS FOR SENTIMENT ANALYSIS
neg_keys = []
pos_keys = []
neg_emote_key = []
pos_emote_keys = []
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


if __name__=="__main__":
	file1 = input("Enter File 1\n")
	file2 = input("Enter File 2\n")
	file3 = input("Enter File 3\n")
	team1 = input("Enter team 1\n")
	team2 = input("Enter team 2\n")


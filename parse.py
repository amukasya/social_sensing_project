#!/usr/bin/env python3


if __name__=="__main__":
	new_list = []
	for line in open("overwatchleague.log"):
		data = line.split()
		new_list.append(data[2:])

	for line in new_list:
		string = (" ").join(line)
		open('new_test_log.txt', 'a').write("%s\n" % string)
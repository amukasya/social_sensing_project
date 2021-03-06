#!/usr/bin/env python3

"""Execute this script and follow the instructions.
First it authorizes the session, so we can login to the chat.
Then we create an irc client. The client will print out messages.
You can also type messages and send them.
To exit, press CTRL-C.
"""
##oauth:01ja2m39fjxc9c92xiy9h17idzajpk
import logging
import sys
import threading
import webbrowser
import queue
import pytwitcherapi

if sys.version_info[0] == 3:
	raw_input = input

log = logging.getLogger("chat")
logging.basicConfig(level=logging.INFO)


master_message_list = []
class IRCClient(pytwitcherapi.IRCClient):
	"""This client will print out private and public messages"""
	def on_pubmsg(self, connection, event):
		super(IRCClient, self).on_pubmsg(connection, event)
		message = self.messages.get()
		log.info('%s: %s' % (message.source.nickname, message.text))
		master_message_list.append(message.text)

	def on_privmsg(self, connection, event):
		super(IRCClient, self).on_pubmsg(connection, event)
		message = self.messages.get()
		log.info('%s: %s' % (message.source.nickname, message.text))

def print_data(arg1, arg2):
	label = "messages_"+str(arg1)+"min_into_game"+str(arg2)
	for messages in master_message_list:
		open(label, 'a').write("%s\n" % messages)


def authorize(session):
	session.start_login_server()
	url = session.get_auth_url()
	webbrowser.open(url)
	raw_input("Please authorize Pytwitcher in the browser then press ENTER!")
	assert session.authorized, "Authorization failed! Did the user allow it?"


def create_client(session):
	channelname = raw_input("Type in the channel to join:")
	channel = session.get_channel(channelname)
	return IRCClient(session, channel)


def main():
	session = pytwitcherapi.TwitchSession()
	authorize(session)
	client = create_client(session)
	t = threading.Thread(target=client.process_forever)
	t.start()
	match = 0
	try:
		while True:
			control = input("n to Start New Match\n")
			if control == "n":
				match += 1
				master_message_list = []
				threading.Timer(180, print_data, ["3",match]).start()
				threading.Timer(480, print_data, ["8",match]).start()
				threading.Timer(720, print_data, ["12",match]).start()
				try:
					m = client.messages.get(block=False)
				except queue.Empty as e:
		 			pass
				else:
					print("Message: %s" % m.text)
	finally:
		client.shutdown()
		t.join()

if __name__ == '__main__':
	main()

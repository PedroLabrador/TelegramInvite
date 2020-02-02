#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from telethon import TelegramClient, sync
from telethon.tl.types import Chat, Channel, InputChannel
from telethon.tl.functions.channels import InviteToChannelRequest
import json, time

# In order to make this script work, set the following variables.
# If you have not a Telegram Application Credentials please go to
# https://my.telegram.org/auth 
# follow this steps https://core.telegram.org/api/obtaining_api_id
# after all done you will be able to set up the next variables.

# Also, you need to specify the file where the usernames are saved
# i suggest you to save then into a json file, 1 per 1 each line
# theres a users.txt file included as an example (you should not 
# try to add those users), if you are not able to create the file
# contact me i'll do it for you, all this are requirements to make 
# the script work :)

# Several things i must say:
# 1. The script is tested on public groups (only groups with Usernames)
# 	 Example: t.me/groupusername
# 				or
# 			  @groupusername
# 2. You have to be aware that users who have not added you to their 
# 	 contact list could report you for spam, i suggest you to create
# 	 a new telegram account for this purposes only if you are not sure
# 	 if the users would report you.
# 	 How do you know if users have reported you? just start a chat 
# 	 with @SpamBot.
# 3. This scripts makes use of "Telethon" python library.
# 4. If any doubt let me know :) @SrPedro at Telegram

api_id = '
api_hash = ''
user_file = 'users.json'

with TelegramClient('session_name', api_id, api_hash) as client:
	client.start()

	with open('users.json') as data_file:
		users = json.load(data_file)

	usernames = []
	for id in users:
		usernames.append(users[id]['username'])

	groupList = list()

	for dialog in client.get_dialogs(limit=10):
		if (isinstance(dialog.entity, Chat) or isinstance(dialog.entity, Channel)):
			groupList.append(dialog.entity)

	for key, group in enumerate(groupList):
		print("[{}]".format(key), group.title)

	try:
		choosenOption = int(input("Please type the number of the group where users will be added: "), 10)
		chat = client.get_input_entity(groupList[choosenOption].id)
		print("\nPreparing user invitations, {} remaining \n".format(len(usernames)))

		remainingUsersToInvite = len(usernames)
		preparedUsers = []
	except Exception as e:
		print("An error has ocurred.")

	while (usernames):
		preparedUsers.append(usernames.pop())
		if (len(preparedUsers) > 13 or (len(usernames) == 0 and len(preparedUsers) > 1)):
			remainingUsersToInvite -= len(preparedUsers)

			try:
				# Prepare the invitation
				result = client(InviteToChannelRequest(
					channel = chat,
					users = preparedUsers
				))
				print("You have invited {} users {} remaining".format(len(preparedUsers), remainingUsersToInvite))
			except Exception as e:
				print ("An user cannot be added :(")

			# Uncomment the next line to display the invited users.
			# print(preparedUsers, len(preparedUsers))
			
			# We sleep the thread for 5 seconds between each user bulk invitation
			# trying to avoid Telegrams spam behaviour.
			time.sleep(5)
			preparedUsers.clear()

	# Single invitation
	#try:
	#	result = client(InviteToChannelRequest(
	#		channel = chat,
	#		users = ['SrPedro']
	#	))
	#except Exception as e:
	#	print ("An user cannot be added :(")
	print("done")


	# READING USERS FROM A GROUP AND WRITING THEM INTO A JSON FILE MUST COMMENT SOME LINES ABOVE
	# data = {}

	# for member in client.get_participants('FromBerek', limit=300):
	# 	memberToAdd = {}
	# 	if (member.username != None and member.bot == False):
	# 		memberToAdd['username'] = member.username
	# 		if (member.first_name != None):
	# 			memberToAdd['first_name'] = member.first_name
	# 		if (member.last_name != None):
	# 			memberToAdd['last_name'] = member.last_name
	# 		data[member.id] = memberToAdd
			
	# with open('users.json', 'w') as outfile:
	# 	json.dump(data, outfile)

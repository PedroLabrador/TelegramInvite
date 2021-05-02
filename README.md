# Telegram Bulk Group Invitation

In order to make this script work, set the following variables.
If you have not a Telegram Application Credentials please go to
https://my.telegram.org/auth 
follow this steps https://core.telegram.org/api/obtaining_api_id
after all done you will be able to set up the next variables.

Also, you need to specify the file where the usernames are saved
i suggest you to save then into a json file, 1 per 1 each line
theres an 'users.json' file included as an example (you should not 
try to add those users), all this to make the script work :)

Several things i must say:
1. The script is tested on public groups (only groups with Usernames)
	 Example: t.me/groupusername
				or
			  @groupusername
2. You have to be aware that users who have not added you to their 
	 contact list could report you for spam, i suggest you to create
	 a new telegram account for this purposes only if you are not sure
	 if the users would report you.
	 How do you know if users have reported you? just start a chat 
	 with @SpamBot.
3. This scripts makes use of "Telethon" python library.

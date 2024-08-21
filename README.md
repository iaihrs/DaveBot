# DaveBot
**DaveBot** reacts to messages from the MediaWiki Discord extension and lets trusted users show their opinions on an edit. 

Trusted users and Whitelisted users are both stored in their own files and are saved over reboots. In info.txt the neccessary variables are placed in the same order and formatting as required by the script. Each should have it's own line and the emotes you want to use must be set as a single string separated by only commas. **info.txt should only contain the parameters asked for!**

Trusted users are on the Discord side of the bot. They are the users able to react to edits posted by the WikiBot. The first trusted user can be added by using .trust which will be accepted by any member. It can also be added manually to trustedUsers.json before the bot is online.

Whitelisted users are on the Wiki side. Whenever they make an edit, the bot will not react to the edits posted by the WikiBot. Whitelisted users can be added by any trusted user.

Both trusted and whitelisted members can be viewed by using their respective commands, which can be viewed by using `.help`.

## Installation
- Make a [discord bot](https://discord.com/developers/applications).
- Go to the OAuth2 tab and in redirects put `https://discordapp.com/oauth2/authorize?&client_id=`CLIENTID`&scope=bot` replacing `CLIENTID` with the Client ID found just above.
- Then go to the URL Generator tab within OAuth2 and add `bot`, `messages.read` and `applications.commands`, and then `Manage Messages` under bot permissions.
- Select your redirect URL and use the Generated URL at the bottom of the page to add the bot to your server.
- Enter the credentials into `info.txt`. (Channel and user IDs require developer mode to be enabled)
  - Secret token, which can be found in the Bot tab by pressing `Reset Token` and entering your 6-digit authentication code
  - Recent Changes channel ID
  - Recent Changes channel name without the #
  - Webhook's user ID
  - Bot's user ID
  - The list of emotes you want to use only separated by commas e.g. 👍,👎,❓,🔥,💀
- From there, just run the bot and it should work fine. It will need to be constantly running to work.

#imports
import discord
import re
import json
import requests
from discord.ext import commands

#perms
intents = discord.Intents.all()

#opens info.txt and creates the variables
with open("info.txt", "r") as f:
        TOKEN = f.readline().rstrip()
        CHANNEL_ID = int(f.readline().rstrip())
        WEBHOOK_ID = int(f.readline().rstrip())
        BOT_USER_ID = int(f.readline().rstrip())
        EMOJIS = f.readline().rstrip().split(",")

#opens trustedUsers.json and makes trustedUsers equal to it's contents
with open('trustedUsers.json') as f:
        trustedUsers = json.load(f)

#opens whitelist.json and makes whitelistedUsers equal to it's contents
with open('whitelist.json') as f:
        whitelistedUsers = json.load(f)

#sets .command thing
client = commands.Bot(command_prefix='.', intents=intents)

#saves files
def saveToFile(obj, filename):
        with open(filename, 'w') as f:
                json.dump(obj, f)
                print(f'{filename} changed')

#hello dave
@client.event
async def on_ready():
        channel = client.get_channel(1158337551367680100)
        await channel.send("*DaveBot is ONLINE*💀💀💀")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="#recent-changes"))

#remove reactions
@client.event
async def on_reaction_add(reaction, user):
        if str(user.id) in trustedUsers:
                for em in EMOJIS:
                        await reaction.message.remove_reaction(em, client.get_user(BOT_USER_ID))

        if str(user.id) not in trustedUsers and user.id != BOT_USER_ID:
                await reaction.remove(client.get_user(user.id))

#waits for message, if the message is in the correct channel id and the webhook sent it checks for the username of the wiki user who made the edit and save it as username, then add these reactions
@client.event
async def on_message(message):
        username = message.content.split(']')[0][1:]
        trustUsername = ''.join(re.findall("[0-9]", message.content))

#checks for right channel, checks that the user is the bot, adds the emojis
        if message.channel.id == CHANNEL_ID and message.author.id == WEBHOOK_ID and username not in whitelistedUsers:
                for em in EMOJIS:
                        await message.add_reaction(em)

#.trust command stuff
        if message.content[:7] == '.trust ' and str(message.author.id) in trustedUsers and trustUsername not in trustedUsers:
                if message.content[8] == '@':
                        trustedUsers.append(trustUsername)
                        await message.channel.send(f"<@{trustUsername}> was added to the trusted user list.")
                else:
                        await message.channel.send("usage: `.trust @DiscordUsername`")

#.untrust command stuff
        if message.content[:9] == '.untrust ' and str(message.author.id) in trustedUsers and trustUsername in trustedUsers:
                if message.content[10] == '@':
                        trustedUsers.remove(trustUsername)
                        await message.channel.send(f"<@{trustUsername}> was removed from the trusted user list.")
                else:
                        await message.channel.send("usage: `.untrust @DiscordUsername`")

#.whitelist add command stuff
        if message.content[:15] == '.whitelist add ' and str(message.author.id) in trustedUsers and message.content.split()[2] not in whitelistedUsers:
                if message.content[16] != '@':
                        whitelistedUsers.append(message.content.split()[2])
                        await message.channel.send(f"{message.content.split()[2]} was added to the whitelist.")
                else:
                        await message.channel.send("usage: `whitelist add WikiUsername`")

#whitelist remove command stuff
        if message.content[:18] == '.whitelist remove ' and str(message.author.id) in trustedUsers and message.content.split()[2] in whitelistedUsers:
                if message.content[19] != '@':
                        whitelistedUsers.remove(message.content.split()[2])
                        await message.channel.send(f"{message.content.split()[2]} was removed from the whitelist.")
                else:
                        await message.channel.send("usage: `whitelist remove WikiUsername`")

#.help command stuff
        if message.content[:5] == '.help':
                await message.channel.send("```.trust @DiscordName - adds user to the trusted list\n.untrust @DiscordName - removes user from the trusted list\n.whitelist add WikiUserName - adds user to the whitelist\n.whitelist remove WikiUserName - removes user from the whitelist\n.trusted - shows a list of all trusted users\n.whitelisted - shows a list of all whitelisted users\n.help - brings up this list of commands```")

#.trusted command stuff
        if message.content[:8] == '.trusted':
                if trustedUsers != []:
                        trustedNameList = ''
                        for tNames in range(len(trustedUsers)):
                                trustedNameList += "`" + str(client.get_user(int(trustedUsers[tNames]))) + "`\n"
                        await message.channel.send("**Trusted users: **\n" + trustedNameList)
                else:
                        await message.channel.send("**There are no trusted users in this server**")

#.whitelisted command stuff
        if message.content[:12] == '.whitelisted':
                if whitelistedUsers != []:
                        whitelistedNameList = ''
                        for wNames in range(len(whitelistedUsers)):
                                whitelistedNameList += "`" + whitelistedUsers[wNames] + "`\n"
                        await message.channel.send("**Whitelisted users: **\n" + whitelistedNameList)
                else:
                        await message.channel.send("**There are no whitelisted users in this server**")

#run the bot, catch any errors and also save to the json files
try:
        client.run(TOKEN)
except KeyboardInterrupt:
        print('keyboard interrupt')
except Exception as e:
        print(e)
finally:
        saveToFile(trustedUsers, 'trustedUsers.json')
        saveToFile(whitelistedUsers, 'whitelist.json')
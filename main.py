import os
from discord.ext import commands
import random
bot = commands.Bot(command_prefix='.')

async def on_ready():
    print ("Ready")

@bot.command(name='roll', help='Sort positions.')
async def roll(ctx, *players):

  if(isinstance(players, list)):
    await ctx.send("players must be a list")
    return

  if ctx.author.voice is None:
    await ctx.send("Connect to voice channel")
    return
  
  roles = [ ":one:", ":two:", ":three:", ":four:", ":five:"]
  channel = ctx.author.voice.channel
  if ctx.voice_client is not None:
    await ctx.voice_client.move_to(channel)
  else:
    await channel.connect()

  print(channel)
  for user in channel.members:
      if not user.bot:
        print(user.name)
  
  players = list(players)
  if(len(players) == 0):
    for userid in channel.voice_states.keys():
      user = await bot.fetch_user(userid)
      if not user.bot:
        players.append(user.name)

  message = ""
  random.shuffle(players)
  for player in players:
    if(len(roles) == 0):
      message += "{} {} \n".format(":x:", player)
      continue
    indexPosition = random.randint(1, len(roles))
    position = roles[indexPosition -1]
    message += "{} {} \n".format(position, player)
    roles.remove(position)

  await ctx.send(message)
  
  return

bot.run(os.getenv('TOKEN'))

# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
import random

description = '''A bot that allows the player to play a rpg maze game'''
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)

maze = [['o','B','x','x','x','x','x','x','x','x'],
        ['x','o','o','o','o','o','o','o','o','x'],
        ['x','o','x','o','x','x','o','x','o','x'],
        ['x','T','x','o','x','x','o','x','o','x'],
        ['x','o','x','x','x','x','o','x','x','x'],
        ['x','o','B','o','o','T','o','B','o','E'],
        ['x','o','x','o','x','x','B','x','o','x'],
        ['x','x','x','x','x','x','x','x','x','x']]

len_x = len(maze)
len_y = len(maze[0])
curr_x = 0
curr_y = 0
hp = 100
xp = 0

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def start(ctx):
    global curr_x, curr_y, hp, xp
    curr_x = 0
    curr_y = 0
    hp = 100
    xp = 0
    await ctx.send("You need to escape this maze: ")
    await ctx.send(printMaze())
    await ctx.send("You are at point P. You need to exit maze(E). You need to fight Boses(B) and get Treasures(T)")
    await ctx.send("You can use left, right, up, down commands to navigate.")
    await ctx.send("Your HP = " + str(hp) + ", XP = " + str(xp))

@bot.command()
async def left(ctx):
    global curr_x, curr_y
    next_x = curr_x
    next_y = curr_y-1
    if (next_y < 0 or maze[next_x][next_y] == 'x'):
        await ctx.send("You can't go this way. Try again.")
    else:
        curr_x = next_x
        curr_y = next_y
        await ctx.send(handleMove())

@bot.command()
async def right(ctx):
    global curr_x, curr_y
    next_x = curr_x
    next_y = curr_y+1
    if (next_y >= len_y or maze[next_x][next_y] == 'x'):
        await ctx.send("You can't go this way. Try again.")
    else:
        curr_x = next_x
        curr_y = next_y
        await ctx.send(handleMove())

@bot.command()
async def up(ctx):
    global curr_x, curr_y
    next_x = curr_x-1
    next_y = curr_y
    if (next_x < 0 or maze[next_x][next_y] == 'x'):
        await ctx.send("You can't go this way. Try again.")
    else:
        curr_x = next_x
        curr_y = next_y
        await ctx.send(handleMove())

@bot.command()
async def down(ctx):
    global curr_x, curr_y
    next_x = curr_x+1
    next_y = curr_y
    if (next_x >= len_x or maze[next_x][next_y] == 'x'):
        await ctx.send("You can't go this way. Try again.")
    else:
        curr_x = next_x
        curr_y = next_y
        await ctx.send(handleMove())
        
def printMaze():
    output = ""
    for i in range(len_x):
        for j in range(len_y):
            if (i == curr_x and j == curr_y):
                output += "P "
            else:
                output += maze[i][j] + " "
        output += '\n'
    return output

def handleMove():
    global hp, xp
    output = ""
    if (maze[curr_x][curr_y] == 'E'):
        output += "Congratulations!! You reached the end.\n"
        output += "You have HP = " + str(hp) + ", XP = " + str(xp)
    elif (maze[curr_x][curr_y] == 'B'):
        hp = hp - random.randint(10, 40)
        xp = xp + random.randint(100, 300)
        output += "You found a boss.\n"
        if (hp <= 0):
            output += "You died!!\n"
        else:
            output += "You have HP = " + str(hp) + ", XP = " + str(xp) + "\n"
        output += printMaze()
    elif (maze[curr_x][curr_y] == 'T'):
        if (random.randint(1,2) == 1):
            hp = hp + 20
            output += "You found a health potion\n"
            output += "You have HP = " + str(hp) + ", XP = " + str(xp) + "\n"
            output += printMaze()
        else:
            xp = xp + 100
            output += "You found a XP\n"
            output += "You have HP = " + str(hp) + ", XP = " + str(xp) + "\n"
            output += printMaze()
    else:
        output += printMaze()
    return output

bot.run('ODA2ODU3OTk2NjI5OTY2ODQ4.YBvjEQ.6NEUYpwnnqdjA72esmeXgxIGKjM')

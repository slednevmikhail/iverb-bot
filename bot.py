import discord
from discord.ext import commands
from main import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['iverb ', 'иверб '])
client = discord.client


@bot.command()
async def скор(ctx, *map_name):
    map_name_string = ' '.join(map_name)
    map_players = get_map_players(map_name_string)
    formatted_string = format_to_string(map_players, map_name_string)
    return await ctx.send(formatted_string)


def format_to_string(map_players_list, map_name):
    result_string = f'```Scores on map {map_name}:\n\n'
    for player in map_players_list:
        result_string += f'{player.rank}. {player.name} - {player.time}\n'
    return result_string + '\n```'


@bot.command()
async def добавить(ctx, player_id):
    if add_player(player_id):
        return await ctx.send('Игрок добавлен')
    return await ctx.send('Иди нахуй')


@bot.command()
async def убрать(ctx, player_id):
    remove_player(player_id)
    return await ctx.send('Игрок убран')


@bot.event
async def on_ready():
    print('My Ready is Body')


bot.run('MTAwODQyNDc3MjQwNjg4NjQ3Mw.G6Mx_t.zq9LLlJht8lMqndTDhEWa6a4f0q3PE7D7_uxWs')

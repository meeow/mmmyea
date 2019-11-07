import discord
import discord_globals 

def player_summary_stats(player_stats: dict) -> discord.Embed:
    embed = discord.Embed(title=player_stats['name'], color=discord_globals.EMBED_COLOR)
    
    # add errors
    err_key = 'error'
    if err_key in player_stats:
        error = player_stats[err_key]
        embed.add_field(
            name=err_key.capitalize(),
            value=error
        )
    # add ratings
    sr_key = 'ratings'
    if sr_key in player_stats:
        ratings = player_stats[sr_key]
        embed.add_field(
            name=sr_key.capitalize(),
            value="\n".join([f"**{role.capitalize()}**: {ratings[role]}" for role in ratings])
        )
    # add most played heroes 
    hero_key = 'heroStats'
    if hero_key in player_stats:
        hero_stats = player_stats[hero_key]
        for hero_info in hero_stats:
            hero_name = list(hero_info.keys())[0]
            embed.add_field(
                name=hero_name.capitalize(),
                value="\n".join([f'{discord_globals.STAT_KEYWORDS[stat]}: {hero_info[hero_name][stat]}' for stat in hero_info[hero_name]])
            )

    return embed
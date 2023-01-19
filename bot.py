from discord.ext import commands
from datetime import datetime
from config import TOKEN, CHANNEL_ID, DISTANCE
from os import system, name
import asyncio
import discord
import geev

client = commands.Bot(command_prefix='+', intents=discord.Intents().all())

def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def get_time(time):
    return f"{time.hour}:{time.minute}"

async def change_presence(total):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{total} annonces envoyées"))

def make_embed(name,distance,link,picture,pfp):
    
    embed=discord.Embed(color=0xf1c40f)
    embed.add_field(
        name=f"""
🧤  **Nom**  :  `{name}`
📍  **Distance**  :  `{distance}`
🕒  **Heure**  :  `{get_time(datetime.now())}`
    """, 
        value=f"🔗 [**Voir**]({link})",
        inline=True
    )
    embed.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/768049100238225418/996af5baea342ee969e131eabd2e70aa.webp?size=80",
        text="Merci d'utiliser mon programme :D"
    )
    embed.set_image(url=picture)
    embed.set_thumbnail(url=pfp)

    return embed

def create_start_embed(channel_name):
    embed=discord.Embed(color=0x3498db)
    embed.add_field(
        name=f"""
🤖  **Status**   : `Démarré`
📩  **Channel**  : `{channel_name}`
📍  **Distance** : `{int(DISTANCE)/1000}km`
""",
        value="[**By ValentinLvrr**](https://github.com/ValentinLvrr)"
    )
    return embed

@client.event
async def on_ready():

    clear()
    channel = client.get_channel(CHANNEL_ID)
    start_embed = create_start_embed(channel.name)
    await channel.send(embed=start_embed)

    sent_items = []

    while True:

        time = get_time(datetime.now())
        print(f"{time} | 📨 | Requete")

        for i in geev.search():
            if i not in sent_items:

                time = get_time(datetime.now())
                embed=make_embed(
                    name = i['name'],
                    distance = i['distance'],
                    link = i['link'],
                    picture = i['picture'],
                    pfp = i['pfp']
                )

                await channel.send(embed=embed)
                sent_items.append(i)
                print(f"{time} | ✅ | Nouvel Item Envoyé ( {i['name']} )")

        await change_presence(total = len(sent_items))
        await asyncio.sleep(60)

client.run(TOKEN)
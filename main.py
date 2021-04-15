import discord
import os
import random

client = discord.Client()


def minecraft_ideator():
    ideas = [
        "Mob Farm", "Slime Farm", "Gunpowder Farm", "Sugarcane Farm",
        "Helicopter", "Witch Farm", "Disco Floor", "Rubiks Cube 3D",
        "Wither Skeleton Farm", "Swimming Pool", "Wheat Field", "Car",
        "Modern House", "Automated Concrete Maker", "Honey and Honeycomb farm",
        "Iron farm", "Automated Brewery", "Villager Trading Hall",
        "Piglin Bartering Farm", "Hoglin Farm", "Zoglin Farm", "Gold Farm",
        "Wood farm", "Giant Tree", "Castle", "Towers", "Automated Item Sorter",
        "Pumpkin and Melon Farm", "Guardian Farm", "Trident Farm",
        "Bubble Elevators", "Elytra Launchpad", "Bouncy Castle",
        "Villager Breeder", "Automatic Door", "Vault for your Richities",
        "Private Jet out of Gold", "Netherite Beacon",
        "Throne of Netherite blocks", "Cliff", "Horse stable", "Snow Mountain",
        "Bunker", "Tank", "Farm House", "Automated Carrot Farm",
        "Automated Potato Farm", "Automated Beetroot Farm",
        "Aquarium of tropical fish", "Cruise", "Boat", "Super Smelter",
        "Cactus Farm", "XP farm", "Temple", "Japanese style Shrine",
        "Greek style Shrine", "Giant Cake", "Mansion", "Tennis Yard",
        "Golf Course", "Stadium", "Movie Theater", "Dining Room",
        "Giant Sphere", "Barn", "Cow Farm", "Sheep Farm", "Blaze Farm"]



    ideaNum = str(len(ideas) - 1)

    idea = "You should build a " + random.choice(
        ideas
    ) + " in your Minecraft world or SMP. I have " + ideaNum + " more unique ideas. Feel free to ask me for more ideas."

    return idea


@client.event
async def on_ready():
    print("Bot has successfully logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(
            "!idea") and message.channel.id == 831457614424309780:
        idea = minecraft_ideator()
        embedVar = discord.Embed(title="",
        description=idea,
        color=990000)
        await message.channel.send(embed=embedVar)


client.run(os.getenv("TOKEN"))

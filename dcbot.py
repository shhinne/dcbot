import discord

# Create a Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# Define a function to handle messages
@client.event
async def on_message(message):
    # Check if the message was sent by the bot itself
    if message.author == client.user:
        return

    # Check if the message starts with the bot's prefix
    if message.content.startswith("!ping"):
        # Send a message back to the user
        await message.channel.send("Hey  bro im alive !")
    if message.content.startswith("!owner "):
       await message.channel.send("Developed by user")
# Start the bot
client.run("bot_token")

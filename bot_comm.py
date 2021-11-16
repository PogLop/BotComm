import discord

token = input("Bot token: ")
client = discord.Client()

@client.event
async def on_ready():
    print("Discord Communication Bot Ready! - made by Hige5897")
    channel_ = input("Channel id: ")
    channel_id = client.get_channel(int(channel_))
    while True:
        message_content = input("Your message: ")
        if message_content != "":
            await channel_id.send(message_content)

client.run(token)
import discord

tkn = input("Token: ")
clnt = discord.Client()

@clnt.event
async def on_ready():
    print("Discord Communication Bot Ready! - made by d3m0n0r")
    channel_ = input("Channel id: ")
    channel_id = clnt.get_channel(int(channel_))
    while True:
        msg_con = input("Message: ")
        if msg_con != "":
            await channel_id.send(msg_con)

clnt.run(tkn)
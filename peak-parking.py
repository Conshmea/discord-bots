import discord
import os
import time

client = discord.Client()

star,P1,P2,P3,P4,P5,P6 = [],[],[],[],[],[],[]
N0 = [star,P1,P2,P3,P4,P5,P6]

N1 = []

N2 = []




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!peak_spots'):
        args = message.content.upper()
        args = args.split(" ")
        
        if len(args) != 1:
            await message.channel.send(f"Usage: !peak_spots")
        else:
            await message.channel.send(f"""{len(star)}/16 spots filled at Star
{len(P1)}/16 spots filled at P1
{len(P2)}/16 spots filled at P2
{len(P3)}/16 spots filled at P3
{len(P4)}/16 spots filled at P4
{len(P5)}/16 spots filled at P5
{len(P6)}/16 spots filled at P6
{len(N1)}/16 spots filled in N1
{len(N2)}/352 spots filled in N2""")

    if message.content.startswith('!peak_locate'):
        args = message.content.upper()
        args = args.split(" ")
        if len(args) != 2:
            await message.channel.send(f"Usage: !peak_locate [carrier_id]")
        else:
            if len(args[1]) == 7 and "-" in args[1]:
                found = 0
                args[1] = args[1].upper()
                for carrier in N2:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at N2")
                        found = 1

                for carrier in N1:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at N1")
                        found = 1

                for carrier in star:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at Star")
                        found = 1

                for carrier in P1:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at P1")
                        found = 1

                for carrier in P2:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at P2")
                        found = 1

                for carrier in P3:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at P3")
                        found = 1

                for carrier in P4:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at P4")
                        found = 1

                for carrier in P5:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at P5")
                        found = 1

                for carrier in P6:
                    carrier = carrier.upper()
                    if args[1] == carrier:
                        await message.channel.send(f"{args[1]} is located at P6")
                        found = 1

                if found != 1:
                    await message.channel.send(f"Unable to locate {args[1]}")
            else:
                await message.channel.send(f"Please use a carrier id")

    if message.content.startswith('!peak_add'):
        args = message.content.upper()
        args = args.split(" ")
        if len(args) != 3:
            await message.channel.send(f"Usage: !peak_add [carrier_id] [body]")
        else:
            args[1] = args[1].upper()
            args[2] = args[2].upper()
            if len(args[1]) == 7 and "-" in args[1]:
                if args[2] != "N2" or "N1" or "STAR" or "P1" or "P2" or "P3" or "P4" or "P5" or "P6":
                    args = message.content.split(" ")
                    if args[2] == "N2":
                        print(args[1])
                        N2.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "N1":
                        N1.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "P1":
                        P1.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "P2":
                        P2.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "P3":
                        P3.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "P4":
                        P4.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "P5":
                        P5.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "P6":
                        P6.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    elif args[2] == "Star":
                        star.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[2]}")
                    else:
                        await message.channel.send(f"""Please use one of the following bodies (Case sensitive).
    Star, P1, P2, P3, P4, P5, P6, N1, N2""")

    if message.content.startswith('!peak_remove'):
        args = message.content.upper()
        args = args.split(" ")
        args[1] = args[1].lower()
        if len(args) != 2:
            await message.channel.send(f"Usage: !peak_remove [carrier_id]")
        else:
            if len(args[1]) == 7 and "-" in args[1]:
                    removed = 0
                    try:
                        N2.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from N2")
                        removed = 1
                    except:
                        pass

                    try:
                        N1.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from N1")
                        removed = 1
                    except:
                        pass

                    try:
                        star.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from Star")
                        removed = 1
                    except:
                        pass

                    try:
                        P1.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P1")
                        removed = 1
                    except:
                        pass

                    try:
                        P2.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P2")
                        removed = 1
                    except:
                        pass

                    try:
                        P3.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P3")
                        removed = 1
                    except:
                        pass

                    try:
                        P4.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P4")
                        removed = 1
                    except:
                        pass

                    try:
                        P5.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P5")
                        removed = 1
                    except:
                        pass

                    try:
                        P6.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P6")
                        removed = 1
                    except:
                        pass

                    if removed == 0:
                        await message.channel.send(f"Could not find carrier: {args[1]} to remove")

    if message.content.startswith('!peak_move'):
        args = message.content.upper()
        args = args.split(" ")
        args[1] = args[1].lower()
        if len(args) != 4:
            await message.channel.send(f"Usage: !peak_remove [carrier_id] [Start_body] [End_body]")
        else:
            if len(args[1]) == 7 and "-" in args[1]:
                    removed = 0
                    try:
                        N2.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from N2")
                        removed = 1
                    except:
                        pass

                    try:
                        N1.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from N1")
                        removed = 1
                    except:
                        pass

                    try:
                        star.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from Star")
                        removed = 1
                    except:
                        pass

                    try:
                        P1.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P1")
                        removed = 1
                    except:
                        pass

                    try:
                        P2.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P2")
                        removed = 1
                    except:
                        pass

                    try:
                        P3.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P3")
                        removed = 1
                    except:
                        pass

                    try:
                        P4.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P4")
                        removed = 1
                    except:
                        pass

                    try:
                        P5.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P5")
                        removed = 1
                    except:
                        pass

                    try:
                        P6.remove(args[1])
                        await message.channel.send(f"{args[1]} removed from P6")
                        removed = 1
                    except:
                        pass

                    if removed == 0:
                        await message.channel.send(f"Could not find carrier: {args[1]} to move")

                    if args[3] == "N2":
                        print(args[1])
                        N2.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "N1":
                        N1.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "P1":
                        P1.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "P2":
                        P2.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "P3":
                        P3.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "P4":
                        P4.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "P5":
                        P5.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "P6":
                        P6.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    elif args[3] == "Star":
                        star.append(args[1])
                        await message.channel.send(f"{args[1]} added to {args[3]}")
                    else:
                        await message.channel.send(f"""Please use one of the following bodies (Case sensitive).
Star, P1, P2, P3, P4, P5, P6, N1, N2""")

                        

               
client.run("[Discord bot token]")

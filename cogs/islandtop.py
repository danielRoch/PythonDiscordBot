import json
import discord
from discord.ext import commands

defaultEmbed = discord.Embed(title="Island Top", description="Island Leader", color=0xFFD700)
defaultEmbed.add_field(name="Moderators", value="Default Mods", inline=False)
defaultEmbed.add_field(name="Members", value="Default Members", inline=False)


# CREATING A CATEGORY AND CHANNEL IN SAID CATEGORY
#
# guild = ctx.guild.id
# await ctx.send("Setting up island top updates!")
# category = await guild.create_category("Island Top", overwrites=None, reason=None)
# await guild.create_text_channel("Retro Island Top", overwrites=None, category=category, reason=None)
# await ctx.send("Setup finished!")

async def isTop_sendMessages(ctx):
    island_top_msg_ids = {}
    msg_ids = {}

    istop_category = await ctx.guild.create_category_channel("Island Top", overwrites=None, reason=None)
    retro_istop_channel = await ctx.guild.create_text_channel("Retro Island Top", overwrites=None,
                                                              category=istop_category, reason=None)

    for i in range(1, 4):
        msg = await retro_istop_channel.send(embed=defaultEmbed)
        msg_ids.update({f"Island Top {i}": str(msg.id)})
    island_top_msg_ids.update({f"{ctx.guild.id}": [msg_ids]})

    with open("island_top_messages_ids.json", "w") as f:
        json.dump(island_top_msg_ids, f, indent=4)
        print("dumped")


class IslandTop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="islandtop", aliases=["istop"], invoke_without_command=True)
    async def islandtop(self, ctx):
        # with open("island_top_messages_ids.json", "r") as f:
        #     island_top_msg_ids = json.load(f)
        #     print(island_top_msg_ids[str(ctx.guild.id)])

        await ctx.send("Please provide a valid context.\nExample: setup")

    # SETUP SUBCOMMAND
    # CHECKS IF THE BOT HAS SENT ISLAND TOP MESSAGES TO THE SERVER
    # IF THE BOT HAS THEN IT WILL LET THE USER KNOW THAT THE SERVER
    # IS RECEIVING UPDATES AND A LINK TO THE MESSAGES
    @islandtop.group(name="setup")
    async def _setup(self, ctx):
        with open("island_top_messages_ids.json", "r") as f:
            island_top_msg_ids = json.load(f)

        if str(ctx.guild.id) not in island_top_msg_ids:
            # if str(ctx.guild.id) in island_top_msg_ids:
            print("Did not find it")

            # guild = ctx.guild.id
            # await ctx.send("Setting up island top updates!")
            # category = await guild.create_category("Island Top", overwrites=None, reason=None, position=None)
            # await guild.create_text_channel("Retro Island Top", overwrites=None, category=category, reason=None)
            # await ctx.send("Setup finished!")

            await isTop_sendMessages(ctx)
        else:
            print("Found it")
            msg_link = await ctx.fetch_message(island_top_msg_ids[str(ctx.guild.id)][0]["Island Top 1"])
            print(msg_link)
            msg_linkURL = msg_link.jump_url
            print(msg_linkURL)
            istop_updatesEmbed = discord.Embed(title="Error",
                                               description=f"This server already is receiving Retro Island Top updates: [HERE]({msg_linkURL})",
                                               color=0x800080)
            istop_updatesEmbed.add_field(name=f"If you wish to create new messages then run the reset subcommand",
                                         value="Example \"--islandtop reset\"", inline=False)
            await ctx.send(embed=istop_updatesEmbed)

    # RESET COMMAND
    @islandtop.group(name="reset")
    async def _reset(self, ctx):
        with open("island_top_messages_ids.json", "r") as f:
            island_top_msg_ids = json.load(f)

        for msg_id in island_top_msg_ids[str(ctx.guild.id)][0].values():
            msg_link = await ctx.fetch_message(msg_id)
            await msg_link.delete()

        island_top_msg_ids.pop[str(ctx.guild.id)][0].values()
        print(island_top_msg_ids)

        with open("island_top_messages_ids.json", "w") as f:
            json.dump(island_top_msg_ids, f, indent=4)

        await isTop_sendMessages(ctx)


def setup(client):
    client.add_cog(IslandTop(client))

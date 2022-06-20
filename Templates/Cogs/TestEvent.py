import discord
from discord.ext import commands

class TestEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention} to the server!!")

def setup(bot):
    bot.add_cog(TestEvent(bot))
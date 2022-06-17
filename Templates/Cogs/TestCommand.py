import discord
from discord.ext import commands

class TestCommand(commands.Cog):
    """
    Test Command Template
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Command()
    async def test_command(self, ctx: commands.Context):
        """
        Test Command
        """
        if ctx.message == "Ping":
            ctx.send("Pong!")

    @test_command.error
    async def test_command_error(self, ctx: commands.Context, error):
        """
        What will happen if the test command errors
        """
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.reply(error)

def setup(bot):
    """
    Required Function to setup this Command
    """
    bot.add_cog(TestCommand(bot))
        
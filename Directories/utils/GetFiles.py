import os
from pathlib import Path

# Should Get config file
configFile = os.path.join(os.path.dirname, "../../Templates/Config/Config.json")

# Cog Command
cogCommand = os.path.join(os.path.dirname, "../../Templates/Cogs/TestCommand.py")

# Cog Event
cogEvent = os.path.join(os.path.dirname, "../../Templates/Cogs/TestEvent.py")

def get_config_file():
    """
    Should Return Config Files with their new places
    """
    return configFile

def get_cog_command():
    """
    Should return Cog Command File Demo
    """
    return cogCommand

def get_cog_event():
    """
    Should Return the demo cog
    """
    pass


    
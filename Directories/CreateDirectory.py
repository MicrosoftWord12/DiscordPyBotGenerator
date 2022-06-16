import os

def createDirs():
    """
    Creates directories for the project
    """
    os.mkdir("src")
    os.mkdir("./src/Utils")
    os.mkdir("./src/Cogs")
    os.mkdir("./src/Cogs/Events")
    os.mkdir("./src/Cogs/Commands")

    return True

    
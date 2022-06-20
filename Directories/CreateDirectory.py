import os

def create_dirs():
    """
    Creates directories for the project
    """
    os.mkdir("src")
    print("Src Folder Created")

    os.mkdir("./src/Utils")
    print("Utils Folder Created")

    os.mkdir("./src/Cogs")
    print("Cogs Folder Created")

    os.mkdir("./src/Cogs/Events")
    print("Cogs, Events Folder Created")

    os.mkdir("./src/Cogs/Commands")
    print("Cogs Commands Folder Created")

    return True

    
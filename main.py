import sys
import os

# def get_app_args():
#     """
#     Gets the Command line arguments the user has sent
#     """
#     return sys.argv[1:]

def get_discord_version():
    """
    Asks the user for their discord version
    """
    print("What discord.py version do you want?\n")
    print("Press Enter if you want the most up to date version\n")
    version = input()
    if version == "":
        os.system("pip install discord.py")

    else:
        os.system(f"pip install discord.py@{version}")

    return version




def run():
    """
    While in development this is how I run the application
    """
    version = get_discord_version()
    print(version)


run()

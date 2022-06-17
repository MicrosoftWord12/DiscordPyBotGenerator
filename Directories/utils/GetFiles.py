import os
from pathlib import Path

# Should Get config file
configFile = os.path.join(os.path.dirname, "../../Templates/Config/Config.json")


def get_config_file():
    """
    Should Return Config Files with their new places
    """
    
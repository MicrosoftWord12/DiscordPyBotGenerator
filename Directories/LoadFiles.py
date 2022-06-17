import os

def get_template_files() -> tuple[list[str], list[str]]:
    """
    Returns the templates files
    """
    config = os.listdir("../Templates/Config")
    cogs = os.listdir("../Templates/Cogs")

    return (config, cogs)

def load_templates_files() -> None:
    """
    @description Adds/Changes the files that you currently have\n
    @Returns Void
    """

    

    cwd = os.getcwd()

    



































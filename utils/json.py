import json
from pathlib import Path


def get_path():
    """
     Gets the current path to the bot.py

     Returns:
         cwd (string) : Path to bot.py directory
    """
    cwd = Path(__file__).parents[1]
    cwd = str(cwd)
    return cwd


def read_json(filename):
    """
    Function to read a json file and return the data

    Parameters:
        filename (string) : Name of the file to open

    Returns:
        Data (dict) : A dict of the data in the file
    """

    cwd = get_path()
    with open(cwd + "/bot_config/" + filename + ".json", "r") as file:
        data = json.load(file)
    return data


def write_json(data, filename):
    """
        Function to write data to a json file

        Parameters:
            data (dict) : The data to write to the file
            filename (string) : Name of the file to open
    """

    cwd = get_path()
    with open(cwd + "/bot_config/" + filename + ".json", "w") as file:
        json.dump(data, file, indent=4)

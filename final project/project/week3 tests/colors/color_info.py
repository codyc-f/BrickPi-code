"""
This file is for any color data related code
It contains the dictionary of RGB values for each color on the map
"""

colors_dictionary = {
    "black": {"mean": [0, 0, 0]},
    "white": {"mean": [300, 300, 200]},
    "yellow": {"mean": [300, 200, 20]},
    "orange": {"mean": [240, 80, 50]},
    "purple": {"mean": [185, 35, 35]},
    "map_white": {"mean": [300, 260, 170]},
    "map_tape": {"mean": [190, 170, 100]},
    "blue": {"mean": [37,60,60]},
    "map_blue_plus_tape": {"mean": [45,50,52]},
    "red": {"mean": [245,38,18]},
    "map_red_plus_tape": {"mean": [250,45,30]},
    "green": {"mean": [37,100,20]},
    "map_green_plus_tape": {"mean": [50,120,30]},
    }

def get_cd() -> dict: 
    return colors_dictionary

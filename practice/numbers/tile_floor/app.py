"""
Find Cost of Tile to Cover W x H Floor - 
Calculate the total cost of tile it would take to cover a floor plan of width and height, 
using a cost entered by the user.
"""

def tile_floor(w: float,h: float,c: float):
    area: float = w * h
    final_cost: float = area * c
    return final_cost 
    
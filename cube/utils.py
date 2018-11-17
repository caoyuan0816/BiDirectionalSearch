"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
utils.py
--------------------------------------------------------------------------------
Tools for rubik cube project.
"""

import random

from cube import Cube

def generateRandomLayout(operationLength):
    """
    Generate a random rubik's cube layout by random operations.
    Support operation types: F,B,R,L,U,D

    Args:
        - operationLength: the length of random operations.

    Return:
        - a string that represent generated cube.
    """
    ops = ['F', 'B', 'R', 'L', 'U', 'D']
    cube = Cube()
    for i in range(operationLength):
        getattr(cube, ops[random.randint(0, 5)])()
    layout = []
    for i in range(6):
        for j in range(3):
            for k in range(3):
                layout.append(cube.cube[i][j][k])
    return ','.join(layout)

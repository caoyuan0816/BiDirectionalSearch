"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
utils.py
--------------------------------------------------------------------------------
Tools for rubik cube project.
"""

import random
import os

from cube import Cube


# Set running path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_PATH)
TEST_PATH = ROOT_PATH + '/test'

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

def generateRandomSingleTest(operationLength, testName):
    """
    Using generateRandomLayout function to generate and store a test case to
    TEST_PATH.
    """
    layout = generateRandomLayout(operationLength)
    with open(TEST_PATH + '/' + testName, 'w') as output:
        output.write(layout)

if __name__ == '__main__':
    generateRandomSingleTest(12, 'rand_12_1')

    generateRandomSingleTest(9, 'rand_12_2')

    generateRandomSingleTest(24, 'rand_12_3')

    generateRandomSingleTest(100, 'rand_12_4')

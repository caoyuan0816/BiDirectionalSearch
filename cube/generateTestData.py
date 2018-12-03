"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
utils.py
--------------------------------------------------------------------------------
Tools for rubik cube project.
"""

import random
import os
import sys

from cube import Cube


# Set running path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_PATH)
TEST_PATH = ROOT_PATH + '/test'

dcti = {'g': 1, 'b': 2, 'r': 3, 'o': 4, 'w': 5, 'y': 6}
ditc = {1: 'g', 2: 'b', 3: 'r', 4: 'o', 5: 'w', 6: 'y'}

def generateRandomLayout(operationLength):
    """
    Generate a random rubik's cube layout by random operations.
    Support operation types: F,B,R,L,U,D

    Args:
        - operationLength: the length of random operations.

    Return:
        - a string that represent generated cube.
    """
    ops = ['F', 'B', 'R', 'L', 'U', 'D', 'rF', 'rB', 'rR', 'rL', 'rU', 'rD']
    cube = Cube()
    for i in range(operationLength):
        rand = random.randint(0, 11)
        #print(ops[rand])
        getattr(cube, ops[rand])()
    return str(cube.getLayout())

def generateRandomSingleTest(operationLength, testName):
    """
    Using generateRandomLayout function to generate and store a test case to
    TEST_PATH.
    """
    layout = generateRandomLayout(operationLength)
    with open(TEST_PATH + '/' + testName, 'w') as output:
        output.write(layout)

def generateRandomMultiTest(operationLength, length, testName):
    base = 'rand_' + str(operationLength) + '_'
    with open(TEST_PATH + '/' + testName, 'w') as output:
        for i in range(length):
            name = base + str(i+1)
            layout = generateRandomLayout(operationLength)
            output.write(name+':'+layout+'\n')


if __name__ == '__main__':
    mode, t, name = sys.argv[1], sys.argv[2], sys.argv[3]
    if mode == 'single':
        generateRandomSingleTest(int(t), name)
    elif mode == 'multi':
        generateRandomMultiTest(int(t), 100, name)

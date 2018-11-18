"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
utils.py
--------------------------------------------------------------------------------
Tools for rubik cube project.
"""

import random
import os
import heapq

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

"""
    data structures from pacman
"""

class Stack:

    def __init__(self):
        self.list = []

    def push(self,item):

        self.list.append(item)

    def pop(self):

        return self.list.pop()

    def isEmpty(self):

        return len(self.list) == 0

class Queue:

    def __init__(self):
        self.list = []

    def push(self,item):

        self.list.insert(0,item)

    def dequeue(self):

        return self.list.pop()

    def isEmpty(self):

        return len(self.list) == 0

class PriorityQueue:

    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    
    #lower priority queue
    def update(self, item, priority):

        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


if __name__ == '__main__':
    generateRandomSingleTest(12, 'rand_12_1')

    generateRandomSingleTest(9, 'rand_12_2')

    generateRandomSingleTest(24, 'rand_12_3')

    generateRandomSingleTest(100, 'rand_12_4')

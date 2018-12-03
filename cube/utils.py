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
    #generateRandomSingleTest(2, 'single_rand_2_1')
    for i in range(1, 13):
        if i < 5:
            generateRandomMultiTest(i, 100, 'multi_rand_'+str(i))
        else:
            generateRandomMultiTest(i, 20, 'multi_rand_'+str(i))


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
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

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
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

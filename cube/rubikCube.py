"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
rubikCube.py
--------------------------------------------------------------------------------
Main entrance for Rubik's Cube project.
There are three primary mode:
    - single test mode: run a single test using given algorithm. In that mode,
        the GUI will be automatically showed.
    - multitest mode: run a set of tests using given algorithm. In that mode,
        we will not show GUI, only print running result for each test layout.

Usage:
Positional arguments:
    mode [single | multi]
    layout [random | layoutName]
    algorithm [BFS | DFS | AS | BI]

Optional arguments:
    -h, --help: to show help message
"""

import os
import argparse
import time

from cube import Cube
import interface
import solver

# Set running path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_PATH)
TEST_PATH = ROOT_PATH + '/test'

# Set arguments parser
parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['single', 'multi'], help='mode of current\
                    running, must be [single | multi].')
parser.add_argument('layout', help='test layout name.')
parser.add_argument('algorithm', choices=['BFS', 'DFS', 'AS', 'BI'],
                    help='algorithm used to solve current cube')
args = parser.parse_args()

if __name__ == '__main__':
    print('Test folder path: {}'.format(
        TEST_PATH
    ))
    print('Running parameters: {}, layout: {}, algorithm: {}\n'.format(
        args.mode, args.layout, args.algorithm
    ))

    try:
        with open(TEST_PATH + '/' + args.layout, 'r') as data:
            # Single mode
            if args.mode == 'single':
                layout = data.readline().strip('\n\r')
                print('Loaded layout: {}: {}\n'.format(args.layout, layout))
                cube = Cube(layout)
                # Try to solve current cube
                print('Solving it using {} algorithm...'.format(args.algorithm))
                solver = getattr(solver, args.algorithm)(cube)

                start = time.time()
                solver.solve()
                end = time.time()

                result = solver.getResult()
                print('Data: {}, Algorithm: {}, Solution: {}, # Node Expanded: {}, Time Used: {}'.format(
                    args.layout, args.algorithm, '->'.join(result), solver.getNodeExpanded(), end-start
                ))
                # Start GUI and run instructions
                interface.runSingleTest(cube, result, 0.3)
            # Multi mode
            else:
                print('Loaded layout: {}\n'.format(args.layout))
                for layout in data.readlines():
                    layout = layout.strip('\n\r')
                    name, layout = layout.split(':')
                    cube = Cube(layout)
                    # Try to solve current cube
                    s = getattr(solver, args.algorithm)(cube)

                    start = time.time()
                    s.solve()
                    end = time.time()

                    result = s.getResult()
                    print('Data: {}, Algorithm: {}, Solution: {}, # Node Expanded: {}, Time Used: {}'.format(
                        name, args.algorithm, '->'.join(result), s.getNodeExpanded(), end-start
                    ))
                    # Start GUI and run instructions
                    #interface.runSingleTest(cube, result, 0.3)

    except IOError:
        print('Error: Cannot open layout file {}'.format(
            TEST_PATH + '/' + args.layout
        ))
        exit()

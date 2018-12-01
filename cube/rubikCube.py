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
    print('Test file path: {}'.format(
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
                solver.solve()
                result = solver.getResult()
                print('Solved! Solution length: {}, Solution: {}, Node Expanded: {}'.format(
                    len(result), '->'.join(result), solver.getNodeExpanded()
                ))
                # Start GUI and run instructions
                interface.runSingleTest(cube, result, 0.3)
            # Multi mode
            else:
                pass

    except IOError:
        print('Error: Cannot open layout file {}'.format(
            TEST_PATH + '/' + args.layout
        ))
        exit()

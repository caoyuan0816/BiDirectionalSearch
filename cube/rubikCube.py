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
    print('Running mode: {}, layout: {}, algorithm: {}'.format(
        args.mode, args.layout, args.algorithm
    ))
    print

    try:
        with open(TEST_PATH + '/' + args.layout, 'r') as data:
            # Single mode
            if args.mode == 'single':
                layout = data.readline().strip('\n\r')
                cube = Cube(layout)
                print('Loaded layout: {}'.format(args.layout))
                # Try to solve current cube
                #TODO
                # Start GUI and run instructions
                interface.runSingleTest(cube, "", 0.3)
            # Multi mode
            else:
                pass

    except IOError:
        print('Error: Cannot open layout file {}'.format(
            TEST_PATH + '/' + args.layout
        ))
        exit()

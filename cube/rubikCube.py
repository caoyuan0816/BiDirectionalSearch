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

# Set running path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_PATH)

# Set arguments parser
parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['single', 'multi'], help='mode of current\
                    running, must be [single | multi].')
parser.add_argument('layout', help='test layout name.')
parser.add_argument('algorithm', choices=['BFS', 'DFS', 'AS', 'BI'],
                    help='algorithm used to solve current cube')
args = parser.parse_args()

if __name__ == '__main__':
    print(ROOT_PATH)
    print(args.mode, args.layout, args.algorithm)

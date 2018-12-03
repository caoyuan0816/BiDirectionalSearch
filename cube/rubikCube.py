"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
rubikCube.py
--------------------------------------------------------------------------------
Main entrance for Rubik's Cube project.
There are two primary mode:
    - single test mode: run a single test using given algorithm. In that mode,
        the GUI will be automatically showed.
    - multitest mode: run a set of tests using given algorithm. In that mode,
        we will not show GUI, only print running result for each test layout.

Usage:
Positional arguments:
    mode [single | multi]
    layout [layoutName]: default test file path is /cube/test
    algorithm [bfs | dfs | astar | bd0 | bd]

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
parser.add_argument('algorithm', choices=['bfs', 'dfs', 'astar', 'bd0', 'bd'],
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
        # Open layout file
        with open(TEST_PATH + '/' + args.layout, 'r') as data:
            # Single mode
            if args.mode == 'single':
                layout = data.readline().strip('\n\r')
                print('Loaded layout: {}: {}\n'.format(args.layout, layout))
                cube = Cube(layout)
                # Try to solve current cube
                print('Solving it using {} algorithm...'.format(args.algorithm))
                maxLengthDFS = int(args.layout.split('_')[-1])

                solver = getattr(solver, args.algorithm)(cube)

                start = time.time()
                solver.solve(maxLengthDFS) if args.algorithm == 'dfs' else solver.solver()
                end = time.time()

                result = solver.getResult()
                print('Data: {}, Algorithm: {}, Solution: {}, # Node Expanded: {}, Time Used: {} (ms)'.format(
                    args.layout, args.algorithm, '->'.join(result), solver.getNodeExpanded(), (end-start)*1000
                ))
                # Start GUI and run instructions
                interface.runSingleTest(cube, result, 0.3)
            # Multi mode
            else:
                print('Loaded layout: {}\n'.format(args.layout))
                maxLengthDFS = int(args.layout.split('_')[-1])
                s_node, s_time, i = 0, 0, 0
                for layout in data.readlines():
                    layout = layout.strip('\n\r')
                    name, layout = layout.split(':')
                    cube = Cube(layout)
                    # Try to solve current cube
                    s = getattr(solver, args.algorithm)(cube)

                    start = time.time()
                    s.solve(maxLengthDFS) if args.algorithm == 'dfs' else s.solve()
                    end = time.time()

                    node, t = s.getNodeExpanded(), end-start
                    s_node += node
                    s_time += t

                    result = s.getResult()
                    print('Data: {}, Algorithm: {}, Solution: {}, # Node Expanded: {}, Time Used: {} (ms)'.format(
                        name, args.algorithm, '->'.join(result), node, t*1000
                    ))
                    i += 1
                    # Start GUI and run instructions
                    #interface.runSingleTest(cube, result, 0.3)
                print()
                print('Data: {}, Algorithm: {}, avg node expanded: {}, avg time: {} (ms)'.format(
                    args.layout, args.algorithm, s_node / i, (s_time / i)*1000
                ))
    except IOError:
        print('Error: Cannot open layout file {}'.format(
            TEST_PATH + '/' + args.layout
        ))
        exit()

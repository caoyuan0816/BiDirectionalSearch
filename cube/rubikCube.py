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
    -m or --mode [single | multi]
    -l or --layout [random | layoutName]
    -a or --algorithm [BFS | DFS | AS | BI]
"""

import os

# Set running path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    print(ROOT_PATH)

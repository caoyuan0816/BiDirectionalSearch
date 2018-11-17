"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
rubikCube.py
--------------------------------------------------------------------------------
Solver functions for rubik's cube problem.
Including:
    BFS solver.
    DFS solver.
    A* solver. (called AS).
    Bi-directional Search solver. (called BI)
"""

from cube import Cube

class Solver:
    """
    Abstract class solver.
    """
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        pass

    def getResult(self):
        return self.result

class BFS(Solver):
    """
    BFS solver.
    """
    def solve(self):
        # TODO
        pass

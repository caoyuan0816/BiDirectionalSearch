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
import copy

from cube import Cube
import utils


class Solver:
    """
    Abstract class solver.
    """
    def __init__(self, cube):
        self.cube = cube
        self.expanded = 0
        self.ops = ['F', 'B', 'R', 'L', 'U', 'D', 'rF', 'rB', 'rR', 'rL', 'rU', 'rD']
        self.rops = ['rF', 'rB', 'rR', 'rL', 'rU', 'rD', 'F', 'B', 'R', 'L', 'U', 'D']

    def solve(self):
        pass

    def getResult(self):
        return self.__parseInstructions(self.result)

    def __parseInstructions(self, instructions):
        """
        """
        res, i = [], 0
        while i < len(instructions):
            if instructions[i] == 'r':
                res.append(instructions[i]+instructions[i+1])
                i += 2
            else:
                res.append(instructions[i])
                i += 1
        return res

    def getNodeExpanded(self):
        return self.expanded


class BFS(Solver):
    """
    BFS solver.
    """
    def solve(self):
        from collections import deque

        visited = set([self.cube.getLayout()])
        que = deque([(self.cube.getLayout(), '')])

        while len(que) != 0:
            cur_layout, cur_ops = que.popleft()
            cur_cube = Cube(cur_layout)

            if cur_cube.isSolved():
                self.result = cur_ops
                self.expanded = len(visited)
                return True

            for o in range(12):
                # Pruning
                if len(cur_ops) != 0 and self.rops[o] == cur_ops[-1]:
                    continue
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited:
                    que.append((layout, cur_ops+self.ops[o]))
                    visited.add(layout)
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False


class DFS(Solver):
    """
    DFS solver.
    """
    def solve(self):
        visited = set([self.cube.getLayout()])
        stack = [(self.cube.getLayout(), '')]

        while len(stack) != 0:
            cur_layout, cur_ops = stack.pop()
            cur_cube = Cube(cur_layout)

            if cur_cube.isSolved():
                self.result = cur_ops
                self.expanded = len(visited)
                return True

            for o in range(12):
                # Pruning
                if len(cur_ops) != 0 and self.rops[o] == cur_ops[-1]:
                    continue
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited:
                    stack.append((layout, cur_ops+self.ops[o]))
                    visited.add(layout)
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False


class BI(Solver):
    """
    Bi-directional Search solver
    """
    def solve(self):
        pass

class AS(Solver):
    """
    Astar solver.
    """
    def __heuristic(self, cube):
        count = 0
        for i in range(6):
            color = cube.cube[i][1][1]
            for j in range(3):
                for k in range(3):
                    if cube.cube[i][j][k] != color:
                        count += 1
        return count

    def solve(self):
        import heapq

        pq = [(self.__heuristic(self.cube), self.cube.getLayout(), '', 0)]
        visited = set([self.cube.getLayout()])

        while len(pq) != 0:
            h, cur_layout, cur_ops, g = heapq.heappop(pq)
            cur_cube = Cube(cur_layout)

            if self.__heuristic(cur_cube) == 0:
                self.result = cur_ops
                self.expanded = len(visited)
                return True

            for o in range(12):
                # Pruning
                if len(cur_ops) != 0 and self.rops[o] == cur_ops[-1]:
                    continue
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited:
                    heapq.heappush(pq, (self.__heuristic(cur_cube)+g, layout, cur_ops+self.ops[o], g+1))
                    visited.add(layout)
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False

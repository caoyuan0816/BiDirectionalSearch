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
        self.ops = ['F', 'B', 'R', 'L', 'U', 'D', 'rF', 'rB', 'rR', 'rL', 'rU', 'rD']
        self.rops = ['rF', 'rB', 'rR', 'rL', 'rU', 'rD', 'F', 'B', 'R', 'L', 'U', 'D']

    def solve(self):
        pass

    def getResult(self):
        return self.result

class BFS(Solver):
    """
    BFS solver.
    """
    def solve(self):
        from collections import deque

        visited = set([self.cube.getLayoutStr()])
        que = deque([(self.cube.getLayoutStr(), '')])

        while len(que) != 0:
            cur_layout, cur_ops = que.popleft()
            cur_cube = Cube(cur_layout)

            if cur_cube.isSolved():
                self.result = cur_ops
                return True

            for o in range(12):
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayoutStr()
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
    def solve(self, visited=None, cube=None, ops=''):
        if cube is None:
            cube = copy.deepcopy(self.cube)
            visited = set(cube.getLayoutStr())

        if cube.isSolved():
            self.result = ops
            return True

        for o in range(12):
            getattr(cube, self.ops[o])()
            layout = cube.getLayoutStr()
            if layout not in visited:
                visited.add(layout)
                if self.solve(visited, cube, ops+self.ops[o]):
                    return True
                #visited.remove(layout)
            getattr(cube, self.rops[o])()
        return False


class BI(Solver):
    """
    Bi-directional Search solver
    """
    def solve(self):
        pass

class AS(Solver):
    """
    A * solver.
    """
    def solve(self):
        # TODO

        queue = utils.PriorityQueue()
        visited = []
        solution = []
        queue.append(copy.deepcopy(self.cube), heuristic(self.cube))

        while len(queue) != 0:

            cur = queue.pop()
            visited.append(copy.deepcopy(self.cube))

            if cur.isSolved():
                solution_str = ','.join(solution)

                return solution_str


            for op in self.ops:
                op
                if self.cube not in visited:
                    solution.append(op)
                    queue.append(copy.deepcopy(self.cube), heuristic(self.cube))

                else:
                    #reverse
                    op
                    op
                    op

                # check reverse ops
                for op in self.ops:
                    op
                    op
                    op
                    if self.cube not in visited:
                        solution.append(op)
                        queue.append(copy.deepcopy(self.cube))

                    else:
                        # reverse
                        op

        return
        #pass






    """
    count how many cubes are different with cube[i][1][1]
    """

    def heuristic(cube):
        count = 0
        for i in range(6):
            color = cube[i][1][1]
            for j in range(3):
                for k in range(3):
                    if cube[i][j][k] != color:
                        count += 1
        return count

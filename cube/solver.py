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

from cube import Cube, utils


class Solver:
    """
    Abstract class solver.
    """
    def __init__(self, cube):
        self.cube = cube
        self.ops = ['F', 'B', 'R', 'L', 'U', 'D' ]

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
        from collections import deque

        visited = []
        que = deque()
        que.append(copy.deepcopy(self.cube))
        solution = []

        while len(que) != 0 :
            cur = que.popleft()
            visited.append(copy.deepcopy(self.cube))
            if cur.isSolved():
                #invert list to str
                solution_str = ','.join(solution)

                return solution_str
            for op in self.ops:
                op
                if self.cube not in visited:
                    solution.append(op)
                    que.append(copy.deepcopy(self.cube))

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
                    que.append(copy.deepcopy(self.cube))

                else:
                    #reverse
                    op

        solution_str = ','.join(solution)

        return solution_str
        #pass


class DFS(Solver):
    """
        DFS solver.
        """
    def solve(self):

        from collections import deque
        stack = deque()

        stack.append(copy.deepcopy(self.cube))
        solution = []
        visited = []

        while len(stack) != 0:
            cur = stack.pop()
            visited.append(copy.deepcopy(self.cube))

            if cur.isSolved():
                solution_str = ','.join(solution)

                return solution_str


            for op in self.ops:
                op
                if self.cube not in visited:
                    solution.append(op)
                    stack.append(copy.deepcopy(self.cube))


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
                        stack.append(copy.deepcopy(self.cube))

                    else:
                        # reverse
                        op
        return
        #pass


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
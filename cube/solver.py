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

class Solver:
    """
    Abstract class solver.
    """
    def __init__(self, cube):
        self.cube = cube
        self.result = None
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


class breadthFirstSearch(Solver):
    """
    BFS solver.
    """
    def solve(self):
        from collections import deque

        if self.cube.isSolved():
            self.result = ''
            return True

        visited = set([self.cube.getLayout()])
        que = deque([(self.cube.getLayout(), '')])

        while len(que) != 0:
            cur_layout, cur_ops = que.popleft()
            cur_cube = Cube(cur_layout)

            for o in range(12):
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited:
                    if Cube(layout).isSolved():
                        self.result = cur_ops+self.ops[o]
                        self.expanded = len(visited)
                        return True
                    visited.add(layout)
                    que.append((layout, cur_ops+self.ops[o]))
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False


class depthFirstSearch(Solver):
    """
    DFS solver.
    """
    def __helper(self, layout, ops, visited, level, maxLevel):
        self.expanded += 1
        cube = Cube(layout)
        if cube.isSolved():
            self.result = ''.join(ops)
            return True
        if level == maxLevel:
            return False

        for o in range(12):
            getattr(cube, self.ops[o])()
            cur_layout = cube.getLayout()
            if cur_layout not in visited:
                visited.add(cur_layout)
                if self.__helper(cur_layout, ops+[self.ops[o]], visited, level+1, maxLevel):
                     return True
                visited.remove(cur_layout)
            getattr(cube, self.rops[o])()

        return False

    def solve(self, maxLevel):
        return self.__helper(self.cube.getLayout(), [], set(), 0, maxLevel)


class aStarSearch(Solver):
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

    def __cost(self, depth):
        return depth*5

    def solve(self):
        import heapq

        if self.__heuristic(self.cube) == 0:
            self.result = ''
            return True

        pq = [(self.__heuristic(self.cube), self.cube.getLayout(), '', 0)]
        visited = set([self.cube.getLayout()])

        while len(pq) != 0:
            h, cur_layout, cur_ops, g = heapq.heappop(pq)
            cur_cube = Cube(cur_layout)

            for o in range(12):
                # Pruning
                if len(cur_ops) != 0 and self.rops[o] == cur_ops[-1]:
                    continue
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited:
                    if self.__heuristic(Cube(layout)) == 0:
                        self.result = cur_ops+self.ops[o]
                        self.expanded = len(visited)
                        return True
                    visited.add(layout)
                    heapq.heappush(pq, (self.__heuristic(cur_cube)+self.__cost(g+1), layout, cur_ops+self.ops[o], g+1))
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False


class biDirectionalSearchMM0(Solver):
    """
    Bi-directional Search solver
    MM0
    """
    def solve(self):
        from collections import deque

        que1, que2 = deque([(self.cube.getLayout(), '', 0)]), deque([(Cube().getLayout(), '', 0)])
        visited1, visited2 = {self.cube.getLayout(): ''}, {Cube().getLayout(): ''}
        expanding_level1, expanding_level2 = 0, 0

        while True:
            if len(que1) == 0:
                self.result = None
                return False
            while len(que1) != 0 and que1[0][2] == expanding_level1:
                cur_layout, cur_ops, level = que1.popleft()
                cur_cube = Cube(cur_layout)

                if cur_layout in visited2:
                    self.result = cur_ops + visited2[cur_layout]
                    self.expanded = len(visited1) + len(visited2)
                    return True

                for o in range(12):
                    getattr(cur_cube, self.ops[o])()
                    layout = cur_cube.getLayout()
                    if layout not in visited1:
                        visited1[layout] = cur_ops+self.ops[o]
                        que1.append((layout, cur_ops+self.ops[o], level+1))
                    getattr(cur_cube, self.rops[o])()
            expanding_level1 += 1

            if len(que2) == 0:
                self.result = None
                return False
            while len(que2) != 0 and que2[0][2] == expanding_level2:
                cur_layout, cur_ops, level = que2.popleft()
                cur_cube = Cube(cur_layout)

                if cur_layout in visited1:
                    self.result = visited1[cur_layout] + cur_ops
                    self.expanded = len(visited1) + len(visited2)
                    return True

                for o in range(12):
                    getattr(cur_cube, self.ops[o])()
                    layout = cur_cube.getLayout()
                    if layout not in visited2:
                        visited2[layout] = self.rops[o]+cur_ops
                        que2.append((layout, self.rops[o]+cur_ops, level+1))
                    getattr(cur_cube, self.rops[o])()
            expanding_level2 += 1

        self.result = None
        return False


class biDirectionalSearchMM(Solver):
    """
    Bi-directional Search solver
    MM0
    """
    def __heuristic(self, cube1, cube2=None):
        if cube2 is None:
            cube2 = Cube()
        count = 0
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    if cube1.cube[i][j][k] != cube2.cube[i][j][k]:
                        count += 1
        return count

    def __cost(self, depth):
        return depth*5

    def solve(self):
        import heapq

        pq1 = [(self.__heuristic(self.cube), self.cube.getLayout(), '', 0)]
        pq2 = [(self.__heuristic(Cube(), self.cube), Cube().getLayout(), '', 0)]

        visited1, visited2 = {self.cube.getLayout(): ''}, {Cube().getLayout(): ''}

        while True:
            if len(pq1) == 0:
                self.result = None
                return False

            _, cur_layout, cur_ops, level = heapq.heappop(pq1)
            cur_cube = Cube(cur_layout)

            if cur_layout in visited2:
                self.result = cur_ops + visited2[cur_layout]
                self.expanded = len(visited1) + len(visited2)
                return True

            for o in range(12):
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited1:
                    visited1[layout] = cur_ops+self.ops[o]
                    np = self.__cost(level+1)+self.__heuristic(cur_cube)
                    heapq.heappush(pq1, (np, layout, cur_ops+self.ops[o], level+1))
                getattr(cur_cube, self.rops[o])()

            if len(pq2) == 0:
                self.result = None
                return False

            _, cur_layout, cur_ops, level = heapq.heappop(pq2)
            cur_cube = Cube(cur_layout)

            if cur_layout in visited1:
                self.result = visited1[cur_layout] + cur_ops
                self.expanded = len(visited1) + len(visited2)
                return True

            for o in range(12):
                getattr(cur_cube, self.ops[o])()
                layout = cur_cube.getLayout()
                if layout not in visited2:
                    visited2[layout] = self.rops[o]+cur_ops
                    np = self.__cost(level+1)+self.__heuristic(cur_cube, self.cube)
                    heapq.heappush(pq2, (np, layout, self.rops[o]+cur_ops, level+1))
                getattr(cur_cube, self.rops[o])()

        self.result = None
        return False

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bd0 = biDirectionalSearchMM0
bd = biDirectionalSearchMM

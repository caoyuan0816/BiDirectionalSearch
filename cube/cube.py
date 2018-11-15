"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
Cube.py
--------------------------------------------------------------------------------
Implementation of class Cube, which used to describe a cube in the real world.
"""

class Cube:
    """
    Class Cube uses a 6*3*3 matrix to store color of a rubik's cube.
    Each row described the color of one side of cube, and these sides ordered by:
        Front -> Back -> Right -> Left -> Up -> Down
    Example:
        [[[g, g, g], [g, g, g], [g, g, g]], //Front(Green)
         [[b, b, b], [b, b, b], [b, b, b]], //Back(Blue)
         [[r, r, r], [r, r, r], [r, r, r]], //Right(Red)
         [[o, o, o], [o, o, o], [o, o, o]], //Left(Orange)
         [[w, w, w], [w, w, w], [w, w, w]], //Up(White)
         [[y, y, y], [y, y, y], [y, y, y]]] //Down(Yellow)
        described a default rubik's cube.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube

    """

    def __init__(self, layout=None):
        """
        Initialize a 3*3 rubik's cube.

        Args:
            layout: optional. Defualt value is None. User can provide a string
                to describe the default layout of rubik's cube. We will not check
                the validity of input layout, please make sure you input a valid
                layout. Example: "g,g,g,g,g,g,g,g,g,b,b,b,b,b,b,b,b,b,r,r,r,r,r,
                r,r,r,r,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y" is
                a valid layout. The order of rows must be same as the cube
                defination above.
        """

        # Neibors of each side
        self._neighbors = [[(4, 2, 0), (4, 2, 1), (4, 2, 2),
                            (2, 0, 0), (2, 1, 0), (2, 2, 0),
                            (5, 0, 2), (5, 0, 1), (5, 0, 0),
                            (3, 2, 2), (3, 1, 2), (3, 0, 2)],
                           [2, 3, 4, 5],
                           [0, 1, 4, 5],
                           [0, 1, 4, 5],
                           [0, 1, 2, 3],
                           [0, 1, 2, 3]]

        # init cube
        if layout is None:
            self.cube = [[['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
                         [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
                         [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
                         [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
                         [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
                         [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]]
        else:
            if len(layout) != 107:
                raise ValueError('input layout invalid.')
            else:
                self.cube = []
                layout = layout.split(',')
                for i in range(6):
                    self.cube.append([])
                    for j in range(3):
                        self.cube[i].append(layout[i*9+j*3:i*9+(j+1)*3])

    def F(self, reverse=False):
        """
        F operation.
        Rotate Front side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube

        Args:
            reverse: optional. Default value is False. When it's True, will do f
                operation instead of F operation.
        """
        # Rotate Front side
        self.cube[0] = zip(*self.cube[0][::-1])
        # Rotate Other 4 sides
        value = []
        for i in range(12):
            pos = self._neighbors[0][i]
            value.append(self.cube[pos[0]][pos[1]][pos[2]])
        value = value[9:] + value[:9]
        for i in range(12):
            pos = self._neighbors[0][i]
            self.cube[pos[0]][pos[1]][pos[2]] = value[i]


    def B(self, reverse=False):
        pass

    def R(self, reverse=False):
        pass

    def L(self, reverse=False):
        pass

    def U(self, reverse=False):
        pass

    def D(self, reverse=False):
        pass

    def isSolved(self):
        """
        Check whether or not current cube has been solved.
        return:
            boolean value True or False.
        """
        for i in range(6):
            color_set = set()
            for j in range(3):
                for k in range(3):
                    color_set.add(self.cube[i][j][k])
            if len(color_set) != 1:
                return False
        return True

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

        # init cube
        if layout is None:
            self.cube = [[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                         [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
                         [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
                         [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
                         [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
                         [[6, 6, 6], [6, 6, 6], [6, 6, 6]]]
        else:
            layout = str(layout)
            if len(layout) != 54:
                raise ValueError('input layout invalid.')
            else:
                self.cube = []
                for i in range(6):
                    self.cube.append([])
                    for j in range(3):
                        self.cube[i].append([])
                        for k in range(3):
                            self.cube[i][j].append(int(layout[i*9+j*3+k]))


    def __str__(self):
        """
        Cube object to string.
        """
        return str(self.cube)


    def __operation(self, side):
        """
        Helper function for F, B, R, L, U, D operation functions.
            __operation(0) is same as F().
            __operation(1) is same as B().
            .
            .
            .
        """
        # Neibors of each side
        neighbors = [[(4, 2, 0), (4, 2, 1), (4, 2, 2),
                      (2, 0, 0), (2, 1, 0), (2, 2, 0),
                      (5, 0, 2), (5, 0, 1), (5, 0, 0),
                      (3, 2, 2), (3, 1, 2), (3, 0, 2)],
                     [(4, 0, 2), (4, 0, 1), (4, 0, 0),
                      (3, 0, 0), (3, 1, 0), (3, 2, 0),
                      (5, 2, 0), (5, 2, 1), (5, 2, 2),
                      (2, 2, 2), (2, 1, 2), (2, 0, 2)],
                     [(4, 2, 2), (4, 1, 2), (4, 0, 2),
                      (1, 0, 0), (1, 1, 0), (1, 2, 0),
                      (5, 2, 2), (5, 1, 2), (5, 0, 2),
                      (0, 2, 2), (0, 1, 2), (0, 0, 2)],
                     [(4, 0, 0), (4, 1, 0), (4, 2, 0),
                      (0, 0, 0), (0, 1, 0), (0, 2, 0),
                      (5, 0, 0), (5, 1, 0), (5, 2, 0),
                      (1, 2, 2), (1, 1, 2), (1, 0, 2)],
                     [(1, 0, 2), (1, 0, 1), (1, 0, 0),
                      (2, 0, 2), (2, 0, 1), (2, 0, 0),
                      (0, 0, 2), (0, 0, 1), (0, 0, 0),
                      (3, 0, 2), (3, 0, 1), (3, 0, 0)],
                     [(0, 2, 0), (0, 2, 1), (0, 2, 2),
                      (2, 2, 0), (2, 2, 1), (2, 2, 2),
                      (1, 2, 0), (1, 2, 1), (1, 2, 2),
                      (3, 2, 0), (3, 2, 1), (3, 2, 2)]]
        # Rotate Front side
        self.cube[side] = [list(x) for x in zip(*self.cube[side][::-1])]
        # Rotate Other 4 sides
        value = []
        for i in range(12):
            pos = neighbors[side][i]
            value.append(self.cube[pos[0]][pos[1]][pos[2]])
        value = value[9:] + value[:9]
        for i in range(12):
            pos = neighbors[side][i]
            self.cube[pos[0]][pos[1]][pos[2]] = value[i]


    def getLayout(self):
        """
        """
        res = 0
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    res += self.cube[i][j][k]
                    res *= 10
        return res // 10


    def F(self):
        """
        F operation.
        Rotate Front side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(0)

    def rF(self):
        """
        Reversed F operation.
        Rotate Front side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(0)
        self.__operation(0)
        self.__operation(0)

    def B(self):
        """
        B operation.
        Rotate Back side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(1)

    def rB(self):
        """
        Reversed B operation.
        Rotate Back side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(1)
        self.__operation(1)
        self.__operation(1)

    def R(self):
        """
        R operation.
        Rotate Right side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(2)


    def rR(self):
        """
        Reversed R operation.
        Rotate Right side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(2)
        self.__operation(2)
        self.__operation(2)


    def L(self):
        """
        L operation.
        Rotate Left side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(3)


    def rL(self):
        """
        Reversed L operation.
        Rotate Left side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(3)
        self.__operation(3)
        self.__operation(3)


    def U(self):
        """
        U operation.
        Rotate Up side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(4)


    def rU(self):
        """
        Reversed U operation.
        Rotate Up side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(4)
        self.__operation(4)
        self.__operation(4)


    def D(self):
        """
        D operation.
        Rotate Down side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(5)

    def rD(self):
        """
        Reversed D operation.
        Rotate Down side by clockwise 90 degree.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
        """
        self.__operation(5)
        self.__operation(5)
        self.__operation(5)


    def isSolved(self):
        """
        Check whether or not current cube has been solved.
        return:
            boolean value True or False.
        """
        for i in range(6):
            color = self.cube[i][1][1]
            for j in range(3):
                for k in range(3):
                    if self.cube[i][j][k] != color:
                        return False
        return True

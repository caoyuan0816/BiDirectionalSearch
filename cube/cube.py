"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
Cube.py
--------------------------------------------------------------------------------
Implementation of class Cube, which used to describe a cube in the real world.
"""


class Cube:
    """
    Class Cube uses a 6*9 matrix to store color of a rubik's cube.
    Each row described the color of one side of cube, and these sides ordered by:
        Front -> Back -> Right -> Left -> Up -> Down
    Example:
        [[g, g, g, g, g, g, g, g, g], //Front(Green)
         [b, b, b, b, b, b, b, b, b], //Back(Blue)
         [r, r, r, r, r, r, r, r, r], //Right(Red)
         [o, o, o, o, o, o, o, o, o], //Left(Orange)
         [w, w, w, w, w, w, w, w, w], //Up(White)
         [y, y, y, y, y, y, y, y, y]] //Down(Yellow)
        described a default rubik's cube.
        See: https://en.wikipedia.org/wiki/Rubik%27s_Cube
    """

    def __init__(self, layout=None):
        """
        Initialize a 3*3 rubik's cube.

        Args:
            layout: optional. Defualt value is None. User can provide a string
                to describe the default layout of rubik's cube. We will not check
                the validity of input layout, please make sure u input a valid
                layout. Example: "g,g,g,g,g,g,g,g,g,b,b,b,b,b,b,b,b,b,r,r,r,r,r,
                r,r,r,r,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y" is a
                valid layout. The order of rows must be same as the cube
                defination above.
        """
        if layout is None:
            self.cube = [['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                         ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                         ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                         ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                         ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                         ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]
        else:
            if len(layout) != 107:
                raise ValueError('input layout invalid.')
            else:
                self.cube = []
                layout = layout.split(',')
                for i in range(6):
                    self.cube.append(layout[i*9:(i+1)*9])

    def F(self, reverse=False):
        pass

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
        """
            travsal each cube faces and compare the first element with the rest elements.
            if they are different, return false;
        """
        for i in range(6):
            face = self.cube[i]
            simple_color = face[0]
            for color in face:
                if color != simple_color:
                    return False
        return True;

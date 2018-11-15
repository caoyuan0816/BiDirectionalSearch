"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
Interface.py
--------------------------------------------------------------------------------
Implementation the game interface of rubik's cube.
"""

from Tkinter import *

from cube import Cube

class Interface(Frame):
    """
    Class Interface used to visualize Rubik's Cube game solving process.
    It is implemmented by GUI library Tkinter.
    To start a gameinterface, just do:
        interface = Interface()
        interface.mainloop()
    """
    def __init__(self, master=None):
        """
        Initialize game Interface.
        """
        self.cubePos = [[[(160, 160), (200, 160), (240, 160)],
                         [(160, 200), (200, 200), (240, 200)],
                         [(160, 240), (200, 240), (240, 240)]],
                        [[(400, 160), (440, 160), (480, 160)],
                         [(400, 200), (440, 200), (480, 200)],
                         [(400, 240), (440, 240), (480, 240)]],
                        [[(280, 160), (320, 160), (360, 160)],
                         [(280, 200), (320, 200), (360, 200)],
                         [(280, 240), (320, 240), (360, 240)]],
                        [[(40, 160), (80, 160), (120, 160)],
                         [(40, 200), (80, 200), (120, 200)],
                         [(40, 240), (80, 240), (120, 240)]],
                        [[(160, 40), (200, 40), (240, 40)],
                         [(160, 80), (200, 80), (240, 80)],
                         [(160, 120), (200, 120), (240, 120)]],
                        [[(160, 280), (200, 280), (240, 280)],
                         [(160, 320), (200, 320), (240, 320)],
                         [(160, 360), (200, 360), (240, 360)]]
                        ]
        self.cubeColor = {'r': 'red', 'b': 'blue', 'y': 'yellow', 'w': 'white',
                          'o': 'orange', 'g': 'green'}
        Frame.__init__(self, master)
        # Set title
        self.master.title('ASU CSE571 Rubik\'s Cube')
        # Set size of window
        self.master.geometry("560x560+10+150")
        # Disable resize
        self.master.resizable(0, 0)
        self.pack()
        self.__createWidgets()

    def __createWidgets(self):
        """
        Create widgets inside window.
        We use absolute positioning to arrange widgets.
        """
        # Widget canvas, used to draw rubik's cube
        self.cv = Canvas(self.master)
        self.cv['bg'] = 'white' # Background color
        self.cv['height'] = '440' # Height of canvas
        self.cv['width'] = '560' # Width of canvas
        self.cv.place(x=0, y=0)
        self.__drawCube(self.cv)

    def __drawCube(self, canvas, cube=None):
        """
        Draw rubik cube in given canvas.
        """
        cube = Cube()
        cube.F()
        for x in range(6):
            for y in range(3):
                for z in range(3):
                    pos = self.cubePos[x][y][z]
                    color = self.cubeColor[cube.cube[x][y][z]]
                    canvas.create_rectangle(pos[0], pos[1], pos[0]+40, pos[1]+40,
                                            fill=color, width='2')


if __name__ == '__main__':
    root = Tk()
    interface = Interface(root)
    root.mainloop()

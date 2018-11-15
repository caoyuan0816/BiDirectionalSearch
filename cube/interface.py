"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
Interface.py
--------------------------------------------------------------------------------
Implementation the game interface of rubik's cube.
"""

from Tkinter import *
import time
import threading

from cube import Cube

class Interface(Frame):
    """
    Class Interface used to visualize Rubik's Cube game solving process.
    It is implemmented by GUI library Tkinter.
    To start a gameinterface, just do:
        interface = Interface()
        interface.mainloop()
    """
    def __init__(self, master=None, cube=None):
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
        self.cube = Cube() if cube is None else cube
        Frame.__init__(self, master)
        # Set title
        self.master.title('ASU CSE571 Rubik\'s Cube')
        # Set size of window
        self.master.geometry("560x560+10+150")
        # Disable resize
        self.master.resizable(False, False)
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
        self.__drawCube()


    def __drawCube(self):
        """
        Draw rubik cube in given canvas.
        """
        for x in range(6):
            for y in range(3):
                for z in range(3):
                    pos = self.cubePos[x][y][z]
                    color = self.cubeColor[self.cube.cube[x][y][z]]
                    self.cv.create_rectangle(pos[0], pos[1], pos[0]+40, pos[1]+40,
                                            fill=color, width='2')

    def runInstructions(self, instructions, interval):
        """
        Run given instructions.
        Example: instructions="LRDULRD"

        interval used to control the time delay between each move.
        """
        for instruction in instructions:
            try:
                getattr(self.cube, instruction)()
            except AttributeError:
                print("Invalid instruction: {}".format(instruction))
                raise ValueError('input instructions invalid.')
            self.__drawCube()
            self.master.update()
            time.sleep(interval)


if __name__ == '__main__':
    root = Tk()
    interface = Interface(root)
    #interface.runInstructions("FLRFDUFLFRFD", 0.3)
    root.after(0, interface.runInstructions, "FLRFDUFLFRFD", 0.3)
    root.mainloop()

""" Multithread Version backup
in class Interface:
    def runInstructions(self, instructions, interval):
        self.queue = Queue.Queue()
        InstructionRunner(self.queue, self, instructions, interval=interval).start()
        self.master.after(100, self.__check_queue)

    def __check_queue(self):
        try:
            msg = self.queue.get(0)
        except Queue.Empty:
            self.master.after(100, self.__check_queue)

class InstructionRunner(threading.Thread):
    def __init__(self, queue, interface, instructions, interval=0.3):
        threading.Thread.__init__(self)
        self.queue = queue
        self.instructions = instructions
        self.interval = interval
        self.interface = interface

    def run(self):
        for instruction in self.instructions:
            print(instruction)
            try:
                getattr(self.interface.cube, instruction)()
            except AttributeError:
                print("Invalid instruction: {}".format(instruction))
                raise ValueError('input instructions invalid.')
            self.interface.drawCube()
            self.interface.master.update()
            time.sleep(self.interval)
        self.queue.put("Finished")
"""

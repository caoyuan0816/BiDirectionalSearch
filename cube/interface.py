"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
Interface.py
--------------------------------------------------------------------------------
Implementation the game interface of rubik's cube.
"""

from Tkinter import *

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
        Frame.__init__(self, master)
        # Set title
        self.master.title('ASU CSE571 Rubik\'s Cube')
        # Set size of window
        self.master.geometry("810x400+10+150")
        # Disable resize
        self.master.resizable(0, 0)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """
        Create widgets inside window.
        We use absolute positioning to arrange widgets.
        """
        # Widget canvas, used to draw rubik's cube
        self.cv = Canvas(self.master)
        self.cv['bg'] = 'white' # Background color
        self.cv['height'] = '400' # Height of canvas
        self.cv['width'] = '540' # Width of canvas
        self.cv.place(x=0, y=0)

if __name__ == '__main__':
    root = Tk()
    interface = Interface(root)
    root.mainloop()

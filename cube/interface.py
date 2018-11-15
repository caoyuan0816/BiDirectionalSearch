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
        Frame.__init__(self, master)
        self.master.title('ASU CSE571 Rubik\'s Cube')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        pass

if __name__ == '__main__':
    interface = Interface()
    interface.mainloop()

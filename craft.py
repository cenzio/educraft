import pyglet
from screen import Window

class MC(object):

    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.window = None

    def run(self):
        if self.window is None:
            self.window = Window(width=self.width, height=self.height, caption='Pyglet', resizable=True, fullscreen=False)
            # Hide the mouse cursor and prevent the mouse from leaving the window.
            self.window.set_exclusive_mouse(True)
            self.window.setup()
            pyglet.app.run()

        else:
            print("This instance already has a display built, don't try to run it twice")
            exit()

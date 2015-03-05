__author__ = 'Kyle'

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget


#_____________________________________________________________________________________________
class FinalWidget(PyGlassWidget):
    """A class for Assignment 3"""

    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment3Widget."""
        super(FinalWidget, self).__init__(parent, **kwargs)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#_____________________________________________________________________________________________
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
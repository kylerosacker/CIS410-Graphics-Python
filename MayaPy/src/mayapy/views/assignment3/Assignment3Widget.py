__author__ = 'Kyle'

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from mayapy.views.assignment3.single import *
from mayapy.views.assignment3.multi import *

#_____________________________________________________________________________________________
class Assignment3Widget(PyGlassWidget):
    """A class for Assignment 3"""

    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment3Widget."""
        super(Assignment3Widget, self).__init__(parent, **kwargs)
        self.singleBtn.clicked.connect(self._handleSingleButton)
        self.multiBtn.clicked.connect(self._handleMultiButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#_____________________________________________________________________________________________
    def _handleSingleButton(self):
        doSingle()

#_____________________________________________________________________________________________
    def _handleMultiButton(self):
        time = self.timeVal.value()
        doMulti(time)

#_____________________________________________________________________________________________
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
__author__ = 'Kyle'

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from mayapy.views.final.scene1 import *
from mayapy.views.final.scene2 import *
from mayapy.views.final.scene3 import *
from mayapy.views.final.scene4 import *
from mayapy.views.final.scene5 import *
from mayapy.views.final.scene6 import *


#_____________________________________________________________________________________________
class FinalWidget(PyGlassWidget):
    """A class for Assignment 3"""

    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment3Widget."""
        super(FinalWidget, self).__init__(parent, **kwargs)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.s1Btn.clicked.connect(self._handleScene1)
        self.s2Btn.clicked.connect(self._handleScene2)
        self.s3Btn.clicked.connect(self._handleScene3)
        self.s4Btn.clicked.connect(self._handleScene4)
        self.s5Btn.clicked.connect(self._handleScene5)
        self.s6Btn.clicked.connect(self._handleScene6)


#_____________________________________________________________________________________________
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

#_____________________________________________________________________________________
    def _handleScene1(self):
        doFirst()
#_____________________________________________________________________________________
    def _handleScene2(self):
        doSecond()
#_____________________________________________________________________________________
    def _handleScene3(self):
        doThird()
#_____________________________________________________________________________________
    def _handleScene4(self):
        doFourth()
#_____________________________________________________________________________________
    def _handleScene5(self):
        doFifth()
#_____________________________________________________________________________________
    def _handleScene6(self):
        doSixth()
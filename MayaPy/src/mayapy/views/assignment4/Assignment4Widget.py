__author__ = 'Kyle'

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from mayapy.views.assignment4.materials import *

#_____________________________________________________________________________________________
class Assignment4Widget(PyGlassWidget):
    """A class for Assignment 4"""

    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment4Widget."""
        super(Assignment4Widget, self).__init__(parent, **kwargs)
        self.tryBtn.clicked.connect(self._handleTry)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.objs = ["Sphere", "Cube", "Cylinder", "Pyramid"]
        self.mats = ["Gold", "Shiny Aluminum", "Red Plastic", "Bubble"]

        #enumerate combo boxes with options
        for i in range(0, len(self.objs)):
            self.objectCombo.insertItem(i,self.objs[i])
        for j in range(0, len(self.mats)):
            self.materialCombo.insertItem(j,self.mats[j])

        #initialize selection
        self.currentObject = None
        self.currentMaterial = None

    def _handleTry(self):
        if self.objectCombo.currentIndex() == 0:
            self.currentObject = objSphere()
        if self.objectCombo.currentIndex() == 1:
            self.currentObject = objCube()
        if self.objectCombo.currentIndex() == 2:
            self.currentObject = objCylinder()
        if self.objectCombo.currentIndex() == 3:
            self.currentObject = objPyramid()


        if self.materialCombo.currentIndex() == 0:
            self.currentMaterial = matGold()
        if self.materialCombo.currentIndex() == 1:
            self.currentMaterial = matShinyAlum()
        if self.materialCombo.currentIndex() == 2:
            self.currentMaterial = matRedPlastic()
        if self.materialCombo.currentIndex() == 3:
            self.currentMaterial = matBubble()


        assignMaterial(self.currentObject, self.currentMaterial)

#_____________________________________________________________________________________________
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')



def objSphere():
    sphere = cmds.polySphere(r=3)
    return sphere

def objCube():
    cube = cmds.polyCube()
    return cube

def objCylinder():
    cylinder = cmds.polyCylinder(r=1)
    return cylinder

def objPyramid():
    pyramid = cmds.polyPyramid()
    return pyramid
# _______________________________________________________________
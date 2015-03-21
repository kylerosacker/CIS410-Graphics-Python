__author__ = 'Kyle'
import nimble
from nimble import cmds
import os

def doSecond():
    filePath = "C:/Users/Kyle/Downloads/x_wing/x_wing.mb"

    cmds.file(filePath, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='x_wing', i=True )
    cmds.select('x_wing:polySurface3')
    cmds.scale(.1,.1,.1)
    cmds.move(0,10,10)
    cmds.setKeyframe(time=1)
    cmds.move(0,10,-10)
    cmds.setKeyframe(time=120)

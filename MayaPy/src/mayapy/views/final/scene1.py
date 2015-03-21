__author__ = 'Kyle'

import nimble
from nimble import cmds
import os

def doFirst():

    filePath = "C:/Users/Kyle/Downloads/x_wing/x_wing.mb"
    filePath2 = "C:/Users/Kyle/Downloads/hangar.mb"

    cmds.file(filePath, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='x_wing', i=True )

    cmds.file(filePath2, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='hangar', i=True )

    cmds.select('hangar:pPyramid2')
    cmds.scale(8,8,10)
    cmds.select('x_wing:polySurface3')
    cmds.scale(.1,.1,.1)
    cmds.rotate(0,-90,0)
    cmds.move(0,3.3,0)
    cmds.setKeyframe(time=1)
    cmds.move(0,6,0)
    cmds.setKeyframe(time=20)
    cmds.move(8,6,0)
    cmds.setKeyframe(time=40)
    cmds.rotate(0,-20,0)
    cmds.setKeyframe(time=60)
    cmds.move(16,6,-11)
    cmds.setKeyframe(time=120)

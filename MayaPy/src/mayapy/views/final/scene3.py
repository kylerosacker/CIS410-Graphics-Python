__author__ = 'Kyle'

import nimble
from nimble import cmds
import os
import time

def doThird():
    filePath3 = "C:/Users/Kyle/Downloads/hangar2.mb"
    filePath4 = "C:/Users/Kyle/Downloads/tie fighter.mb"
    cmds.file(filePath3, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='hangar2', i=True )

    cmds.select('hangar2:pCube2')
    cmds.move(0,2.872,0)
    cmds.setKeyframe(time=1)

    cmds.file(filePath4, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='tie fighter', i=True )

    cmds.select('tie_fighter:Tie_Droid:polySurface9')
    cmds.scale(.25,.25,.25)
    cmds.move(.8,5.6,0)
    cmds.setKeyframe(time=1)
    cmds.move(.8,5.6,0)
    cmds.setKeyframe(time=15)
    cmds.move(.8,5.6,0)
    cmds.setKeyframe(time=30)
    cmds.move(.8,3.759,0)
    cmds.setKeyframe(time=45)
    cmds.rotate(0,40,0)
    cmds.setKeyframe(time=65)
    cmds.move(4.765,3.759,3.545)
    cmds.setKeyframe(time=90)
    cmds.move(13.514,3.759,12.571)
    cmds.setKeyframe(time=120)

    cmds.file(filePath4, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='tie fighter1', i=True )

    cmds.select('tie_fighter1:Tie_Droid:polySurface9')
    cmds.scale(.25,.25,.25)
    cmds.move(-.2,5.6,0)
    cmds.setKeyframe(time=1)
    cmds.setKeyframe(time=15)
    cmds.move(-.2,4.377,0)
    cmds.setKeyframe(time=30)
    cmds.setKeyframe(time=45)
    time.sleep(1)
    cmds.rotate(0,40,0)
    time.sleep(1)
    cmds.setKeyframe(time=65)
    cmds.move(3.765,4.377,3.545)
    cmds.setKeyframe(time=90)
    cmds.move(12.514,4.377,12.571)
    cmds.setKeyframe(time=120)
    time.sleep(1)

    cmds.file(filePath4, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='tie fighter2', i=True )

    cmds.select('tie_fighter2:Tie_Droid:polySurface9')
    cmds.scale(.25,.25,.25)
    cmds.move(-1.2,5.6,0)
    cmds.setKeyframe(time=1)
    cmds.move(-1.2,3.729,0)
    cmds.setKeyframe(time=15)
    cmds.setKeyframe(time=30)
    cmds.setKeyframe(time=45)
    time.sleep(1)
    cmds.rotate(0,40,0)
    time.sleep(1)
    cmds.setKeyframe(time=65)
    cmds.move(2.765,3.729,3.545)
    cmds.setKeyframe(time=90)
    cmds.move(11.514,3.729,12.571)
    cmds.setKeyframe(time=120)
    time.sleep(1)

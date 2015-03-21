__author__ = 'Kyle'

import nimble
from nimble import cmds
import os

def doFourth():
    filePath4 = "C:/Users/Kyle/Downloads/tie fighter.mb"
    filePath = "C:/Users/Kyle/Downloads/x_wing/x_wing.mb"

    cmds.file(filePath, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='x_wing', i=True )

    cmds.file(filePath4, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='tie fighter', i=True )
    cmds.file(filePath4, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='tie fighter', i=True )
    cmds.file(filePath4, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='tie fighter', i=True )

    cmds.select('x_wing:polySurface3')
    cmds.scale(.15,.15,.15)
    cmds.move(0,4,15)
    cmds.setKeyframe(time=1)
    cmds.move(0,4,11.7)
    cmds.rotate(0,-18.6,0)
    cmds.setKeyframe(time=30)
    cmds.move(6.667, 4.803,7.37)
    cmds.rotate(0,36,0)
    cmds.setKeyframe(time=60)
    cmds.move(-2.127, 6.86,-5.277)
    cmds.rotate(26.244,36,0)
    cmds.setKeyframe(time=120)

    cmds.select('tie_fighter:Tie_Droid:polySurface9')
    cmds.move(2,6,5)
    cmds.rotate(0,180,0)
    cmds.setKeyframe(time=1)
    cmds.move(5,6,1.415)
    cmds.rotate(0,156.849,0)
    cmds.setKeyframe(time=30)
    cmds.move(2.309,8.410,-1.272)
    cmds.rotate(0,214,0)
    cmds.setKeyframe(time=60)
    cmds.move(-7.6,8.410,-15.8)
    cmds.rotate(15,211,-27)
    cmds.setKeyframe(time=120)

    cmds.select('tie_fighter1:Tie_Droid:polySurface9')
    cmds.move(0,4,5)
    cmds.rotate(0,180,0)
    cmds.setKeyframe(time=1)
    cmds.move(3.6,4,1.49)
    cmds.rotate(0,153.924,0)
    cmds.setKeyframe(time=30)
    cmds.move(.64,6.118,-.19)
    cmds.rotate(0,212.91,0)
    cmds.setKeyframe(time=60)
    cmds.move(-9.9,6.118,-14.19)
    cmds.rotate(14.932,209.673,-28.310)
    cmds.setKeyframe(time=120)

    cmds.select('tie_fighter2:Tie_Droid:polySurface9')
    cmds.move(4,4,5)
    cmds.rotate(0,180,0)
    cmds.setKeyframe(time=1)
    cmds.move(7.45,4,1)
    cmds.rotate(0,159.3,0)
    cmds.setKeyframe(time=30)
    cmds.move(4,5.92,-2.743)
    cmds.rotate(0,222.231,0)
    cmds.setKeyframe(time=60)
    cmds.move(-6.65,5.92,-17.742)
    cmds.rotate(8,219,-19.8)
    cmds.setKeyframe(time=120)


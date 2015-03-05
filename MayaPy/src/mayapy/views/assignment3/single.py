__author__ = 'Kyle'


import nimble
from nimble import cmds

#_____________________________________________________________________________________________
def doSingle():

    #keyframes a bubble, does NOT use slider
    r=.1
    c = cmds.polySphere(r=r)
    cmds.setAttr(c[0]+".visibility",0)
    cmds.setKeyframe(time=60)
    cmds.scale(11,10,11)
    cmds.move(0,20,0)
    cmds.setKeyframe(time=50)
    cmds.setAttr(c[0]+".visibility",1)
    cmds.rotate(100,0,0)
    cmds.scale(10,9,9.5)
    cmds.setKeyframe(time=40)
    cmds.move(4,10,0)
    cmds.rotate(60,0,0)
    cmds.setKeyframe(time=30)
    cmds.move(0,6,0)
    cmds.rotate(0,0,0)
    cmds.setKeyframe(time=20)
    cmds.move(0,3,0)
    cmds.scale(3,3,3)
    cmds.setKeyframe(time=10)
    cmds.move(0,0,0)
    cmds.scale(1,.8,1)
    cmds.setKeyframe(time=1)
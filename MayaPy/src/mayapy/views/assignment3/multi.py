__author__ = 'Kyle'


import nimble
from nimble import cmds
from random import randint

#_____________________________________________________________________________________________
def doMulti(time):


   for i in range(0,time/2):
       #makes time/2 bubbles and sets up a bunch of random stats for them
        initTime = randint(0,time-30)
        initX = randint(-10,10)
        initZ = randint(-10,10)
        xRand = randint(-5,5)
        zRand = randint(-5,5)

        #keyframes all the bubbles based on time that user sets in Qt slider
        r=.1
        c = cmds.polySphere(r=r)
        cmds.setAttr(c[0]+".visibility",0)
        cmds.setKeyframe(time = initTime+60)
        cmds.scale(11,10,11)
        cmds.move(initX,20,initZ)
        cmds.setKeyframe(time = initTime+50)
        cmds.setAttr(c[0]+".visibility",1)
        cmds.rotate(100,0,0)
        cmds.scale(10,9,9.5)
        cmds.setKeyframe(time = initTime+40)
        cmds.move(initX+xRand,10,initZ+zRand)
        cmds.rotate(60,0,0)
        cmds.setKeyframe(time = initTime+30)
        cmds.move(initX,6,initZ)
        cmds.rotate(0,0,0)
        cmds.setKeyframe(time=initTime+20)
        cmds.move(initX,3,initZ)
        cmds.scale(3,3,3)
        cmds.setKeyframe(time = initTime+10)
        cmds.move(initX,0,initZ)
        cmds.scale(1,.8,1)
        cmds.setKeyframe(time = initTime)
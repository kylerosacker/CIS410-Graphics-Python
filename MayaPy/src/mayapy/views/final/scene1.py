__author__ = 'Kyle'

import nimble
from nimble import cmds
import os

def doFirst():

    filePath = "C:/Users/Kyle/Downloads/x_wing/x_wing.mb"

    cmds.file(filePath, type='mayaBinary', ra=True, mergeNamespacesOnClash=False, namespace='x_wing', i=True )

__author__ = 'Kyle'
import nimble
from nimble import cmds
import os
import time

def matGold():
    gold = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr(gold+'.color',0.92,0.74,0.05, type='double3')
    cmds.setAttr(gold+'.diffuse',0.47)
    cmds.setAttr(gold+'.translucence',0)
    cmds.setAttr(gold+'.translucenceDepth',0)
    cmds.setAttr(gold+'.translucenceFocus',0)
    cmds.setAttr(gold+'.eccentricity',0.4)
    cmds.setAttr(gold+'.specularRollOff',0.7)
    cmds.setAttr(gold+'.specularColor',0.9,0.72,0.05, type='double3')
    cmds.setAttr(gold+'.reflectivity',0.239)
    cmds.setAttr(gold+'.reflectedColor',0.92,0.74,0.05, type='double3')
    return gold

def matShinyAlum():
    alum = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr(alum+'.color',0.6,0.6,0.6, type='double3')
    cmds.setAttr(alum+'.diffuse',0.44)
    cmds.setAttr(alum+'.translucence',0)
    cmds.setAttr(alum+'.translucenceDepth',0)
    cmds.setAttr(alum+'.translucenceFocus',0)
    cmds.setAttr(alum+'.eccentricity',0.419)
    cmds.setAttr(alum+'.specularRollOff',0.684)
    cmds.setAttr(alum+'.specularColor',1,1,1, type='double3')
    cmds.setAttr(alum+'.reflectivity',0.1)
    cmds.setAttr(alum+'.reflectedColor',0.22,0.22,0.22, type='double3')
    return alum

def matRedPlastic():
    red = cmds.shadingNode('phongE', asShader=True)
    cmds.setAttr(red+'.color',0.77,0,0.03, type='double3')
    cmds.setAttr(red+'.diffuse',0.752)
    cmds.setAttr(red+'.reflectivity',0.684)
    cmds.setAttr(red+'.reflectedColor',0.68,0.47,0.48, type='double3')
    return red

def matBubble():
    bub = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr(bub+'.color',0.16,0.45,0.45, type='double3')
    cmds.setAttr(bub+'.transparency',0.74,0.74,0.74, type='double3')
    cmds.setAttr(bub+'.ambientColor',0.2,0.2,0.2, type='double3')
    cmds.setAttr(bub+'.diffuse',0.8)
    cmds.setAttr(bub+'.translucence',0.658)
    cmds.setAttr(bub+'.eccentricity',0.3)
    cmds.setAttr(bub+'.specularRollOff',0.7)
    cmds.setAttr(bub+'.specularColor',1,1,1, type='double3')
    cmds.setAttr(bub+'.reflectivity',0.5)
    cmds.setAttr(bub+'.reflectedColor',.13,.13,.13, type='double3')
    return bub

def assignMaterial(obj, mat):
    cmds.HypershadeWindow()
    time.sleep(5)
    cmds.select(obj)
    cmds.hyperShade(a = mat)
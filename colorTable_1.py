import pymel.core as pm
import random
import maya.cmds as cmds


lightIntensity = 2
lightExporure = 4


lightColorIndex = {0:[0.0,0.0,0.0],
                   1:[0.0,0.0,0.0],
                   2:[0.0,0.0,0.0],
                   3:[1.0,0.0,1.0],
                   4:[1.0,0.0,0.0],
                   5:[0.0,1.0,0.0],
                   6:[0.0,0.0,1.0],
                   7:[1.0,1.0,0.0],
                   9:[0.0,1.0,1.0]
                   }

lightShapeListy = cmds.ls('*PxrSphereLightShape*',type= 'PxrSphereLight')   # get PxrSphereLights from the name begin "PxrSphereLightShape", and nodeType is PxrSphereLight

for lightShape in lightShapeListy:
    pm.setAttr('%s.intensity'%lightShape,lightIntensity)  #set light intensity 
    pm.setAttr('%s.exposure'%lightShape,lightExporure)  #set light exposure 
    
    
                   
                   

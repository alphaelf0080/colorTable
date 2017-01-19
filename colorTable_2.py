import pymel.core as pm
import random
import maya.cmds as cmds


lightIntensity = 2
lightExporure = 4


lightColorIndex = {1:[0.02,0.01,0.0],
                   2:[0.0,0.02,0.02],
                   3:[0.0,0.02,0.0],
                   4:[1.0,0.0,1.0],
                   5:[1.0,0.0,0.0],
                   6:[0.0,1.0,0.0],
                   7:[0.0,0.0,1.0],
                   8:[1.0,1.0,0.0],
                   9:[0.0,1.0,1.0]
                   }


lightColorIndexEdge = {1:[1.0,0.185,0.0],
                   2:[0.004,0.185,0.0],
                   3:[0.254,0.015,0.056],
                   4:[0.017,0.072,0.144],
                   5:[0.254,0.472,0.056],
                   }



lightShapeList = cmds.ls('*PxrSphereLightShape*',type= 'PxrSphereLight')   # get PxrSphereLights from the name begin "PxrSphereLightShape", and nodeType is PxrSphereLight
lightEdgeShapeList = cmds.ls('*PxrEdgeSphereLight*',type= 'PxrSphereLight')   # get PxrSphereLights from the name begin "PxrSphereLightShape", and nodeType is PxrSphereLight
#pm.select(lightShapeList)
lightCubeShapeList =  cmds.ls('*PxrConstant*',type= 'PxrConstant')    
edgeCubeShapeList = cmds.ls('PxrConstant34')

'''
for lightShape in lightShapeListy:
    
    choseColor = random.randrange(1,9,1)
    print choseColor
    pm.setAttr('%s.intensity'%lightShape,lightIntensity)  #set light intensity 
    pm.setAttr('%s.exposure'%lightShape,lightExporure)  #set light exposure 
   # print lightColorIndex[int(choseColor)]
    
   # print lightColorIndex[choseColor][0],lightColorIndex[choseColor][1],lightColorIndex[choseColor][2]
    
    
    
    print cmds.setAttr('%s.lightColor'%lightShape,lightColorIndex[choseColor][0],lightColorIndex[choseColor][1],lightColorIndex[choseColor][2],type='double3')
    

for emitColor in lightCubeShapeList:
    choseColor = random.randrange(1,9,1)   
    cmds.setAttr('%s.emitColor'%emitColor,lightColorIndex[choseColor][0],lightColorIndex[choseColor][1],lightColorIndex[choseColor][2],type='double3')
    
    
'''    
 
#pm.select(lightShapeList)                


startKeyFrame =  int( 120  )
endKeyFrame=int( 400)
stepByChangeColor =20
keyFrameNums= []
for num in range(startKeyFrame,endKeyFrame):
   # print num
    if num % stepByChangeColor == 0:
        keyFrameNums.append(int(num))
        
print keyFrameNums[0]   ,type(keyFrameNums[0])      
lightCubeShapeList =  cmds.ls('*PxrConstant*',type= 'PxrConstant')           
frameNow = startKeyFrame        
pm.cutKey( lightCubeShapeList,at= 'emitColor',cl=True )  
pm.cutKey( edgeCubeShapeList,at= 'emitColor',cl=True )     
pm.cutKey( lightShapeList,at= 'lightColor',cl=True )     
pm.cutKey( lightEdgeShapeList,at= 'lightColor',cl=True )   
while frameNow < endKeyFrame :
    pm.currentTime (frameNow, e = True)
   # pm.setKeyframe(lightCubeShapeList,at= 'emitColor')
   
  # print frameNow
  # frameNow = frameNow +1
   # cmds.setAttr('%s.emitColor'%emitColor,lightColorIndex[choseColor][0],lightColorIndex[choseColor][1],lightColorIndex[choseColor][2],type='double3')

  ##  pm.setKeyframe(lightCubeShapeList,at= 'emitColor')
 #   pm.setKeyframe('PxrConstant34',at= 'emitColor')
    pm.setKeyframe(lightShapeList,at= 'lightColor')
    pm.setKeyframe(lightEdgeShapeList,at= 'lightColor')
    frameNow = frameNow +1        
        
    
    
    if frameNow in keyFrameNums:
      #  print "BBBBB" + str(frameNow )
       # try:
    #    for emitColor in lightCubeShapeList:
    #        choseColor = random.randrange(1,9,1)           
    #        choseColorEdge = random.randrange(1,5,1)   
    #        cmds.setAttr('%s.emitColor'%emitColor,lightColorIndex[choseColor][0],lightColorIndex[choseColor][1],lightColorIndex[choseColor][2],type='double3')
            
            
      #      cmds.setAttr('PxrConstant34.emitColor',lightColorIndexEdge[choseColorEdge][0],lightColorIndexEdge[choseColorEdge][1],lightColorIndexEdge[choseColorEdge][2],type='double3')
        for lightColorA in lightShapeList:
            choseColor = random.randrange(1,9,1)           
            choseColorEdge = random.randrange(1,5,1)   
            cmds.setAttr('%s.lightColor'%lightColorA,lightColorIndex[choseColor][0],lightColorIndex[choseColor][1],lightColorIndex[choseColor][2],type='double3')
            
        for lightColorE in lightEdgeShapeList:
            cmds.setAttr('%s.lightColor'%lightColorE,lightColorIndexEdge[choseColorEdge][0],lightColorIndexEdge[choseColorEdge][1],lightColorIndexEdge[choseColorEdge][2],type='double3')
#
           


       # except:
        #    pass
   #     pm.setKeyframe(lightCubeShapeList,at= 'emitColor')
    #    pm.setKeyframe('PxrConstant34',at= 'emitColor')
        pm.setKeyframe(lightShapeList,at= 'lightColor')
        pm.setKeyframe(lightEdgeShapeList,at= 'lightColor')

        
        frameNow = frameNow +1
        


        

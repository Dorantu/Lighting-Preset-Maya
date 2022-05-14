# LIGHTING PRESETS 

import maya.cmds as cmds

# MAIN CODE ---------------------------------------


# window
LightPresetWindow = cmds.window(title="Portrait Painting | Lighting Presets" )
cmds.columnLayout(adjustableColumn=True)

# text a the top explaining the program
cmds.separator(h=50)
cmds.text("  Please select your 3D model, then choose a preset here, so the lights can be placed around your model.  ")
cmds.text("  Please make sure your model is facing the Z forward direction.  ")

cmds.separator(h=25)
cmds.button( label='Delete all the existing lights in the scene', command="DeleteAllLights()")
cmds.separator(h=25)

# buttons

cmds.button( label= 'La Jeune Fille ' u'\u00e0'  ' la perle - Vermeer', command="vermeer()")
cmds.button( label= 'Le D' u'\u00e9' 'sesp' u'\u00e9' 'r' u'\u00e9' '- Courbet', command="desespere()")
cmds.button( label='La Naissance de V' u'\u00e9' 'nus - Botticelli', command="naissance()")
cmds.button( label='Jeune femme dessinant - Marie-Denise Villers', command="dessinant()")
cmds.button( label='Le joueur de luth - Caravage', command="luth()")
cmds.button( label='Le Nouveau-N' u'\u00e9' ' - De La Tour', command="nouveau()")
cmds.button( label='Homme au gant - Titian', command="gant()")
cmds.button( label='La Belle Ferronni' u'\u0065' 're - Leonardo Da Vinci', command="ferronniere()")
cmds.button( label = 'Spleen et id' u'\u00e9' 'al - Carlos Schwabe', command = "spleenEtIdeal()")
cmds.separator(h=50)

# show the window
cmds.showWindow()


# FUNCTIONS ---------------------------------------

def vermeer():
     
    # save the selection
    myModel = cmds.ls( sl=True) 
    
    # we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)
    
    # light Top Left
    lamp1Name = cmds.directionalLight(intensity=2)
    cmds.move(bb[0], bb[4]*0.60, bb[5])
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 0)
    
    # light filler Bottom Right
    lamp2Name = cmds.directionalLight(intensity=0.25)
    cmds.move(bb[3], bb[1]*0.60, bb[5])
    lamp2 = cmds.ls( sl=True)
    cmds.setAttr(lamp2Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp2Name + ".aiAngle", 0)
    
    
    # we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp2, aimVector= (0, 0, -1))
    

def desespere():
    
    # save the selection
    myModel = cmds.ls( sl=True) 
    
    # we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)

    # light Top Left
    lamp1Name = cmds.directionalLight(intensity=4)
    cmds.move(bb[0], bb[4]*1.25, bb[2])
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 0)
    
    # light filler Bottom Right
    lamp2Name = cmds.directionalLight(intensity=0.5)
    cmds.move((bb[0]+bb[3])/2 , (bb[1]+bb[4])/2, bb[5]*1.50)
    lamp2 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 0)
    
    # we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp2, aimVector= (0, 0, -1))
  
  
def naissance(): 

    # save the selection
    myModel = cmds.ls( sl=True) 
    
    # we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)
    
    # light Right
    lamp1Name = cmds.directionalLight(intensity=3.5)
    cmds.move(bb[3]*0.90, (bb[1] + bb[4])/2, bb[5]*3)
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.2 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 5)

    # light filler
    lamp2Name = cmds.directionalLight(intensity=0.1)
    cmds.move(bb[0], (bb[1] + bb[4])/2, bb[5])
    lamp2 = cmds.ls( sl=True)
    cmds.setAttr(lamp2Name + ".aiShadowDensity",0.2 ) 
    cmds.setAttr(lamp2Name + ".aiAngle", 5)
    cmds.setAttr(lamp2Name + ".color", 1, 1, 0, type="double3")
    
    
    # we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp2, aimVector= (0, 0, -1))
    
def dessinant(): 

    # save the selection
    myModel = cmds.ls( sl=True) 
    
    #we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)
    
    #light back 1
    lamp1Name = cmds.directionalLight(intensity=25)
    cmds.move((bb[0]+bb[3])/2, (bb[1] + bb[4])/3, bb[2]*2)
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.2 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 5)
    
    #light back 2
    lamp2Name = cmds.directionalLight(intensity=10)
    cmds.move((bb[0]+bb[3])/2, (bb[1] + bb[4])/1.5, bb[2]*2)
    lamp2 = cmds.ls( sl=True)
    cmds.setAttr(lamp2Name + ".aiShadowDensity",0.2 ) 
    cmds.setAttr(lamp2Name + ".aiAngle", 5)
    
    #light front
    lamp3Name = cmds.directionalLight(intensity=1)
    cmds.move((bb[0]+bb[3])/2, (bb[1] + bb[4])/4, bb[5]*2)
    lamp3 = cmds.ls( sl=True)
    cmds.setAttr(lamp3Name + ".aiShadowDensity",0.2 ) 
    cmds.setAttr(lamp3Name + ".aiAngle", 5)
    
     #we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp2, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp3, aimVector= (0, 0, -1))
    
def luth():
     
    #save the selection
    myModel = cmds.ls( sl=True) 
    
    #we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)
    
    #light Top Left
    lamp1Name = cmds.directionalLight(intensity=1.75)
    cmds.move(bb[0], bb[4]*0.70, bb[5]*0.75)
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 0)
    
    
    #light RED filler Bottom Right
    lamp2Name = cmds.directionalLight(intensity=0.75)
    cmds.move(bb[3]*0.75, bb[1]*0.60, bb[5])
    lamp2 = cmds.ls( sl=True)
    cmds.setAttr(lamp2Name + ".aiShadowDensity",0.02 ) 
    cmds.setAttr(lamp2Name + ".aiAngle", 0)
    cmds.setAttr(lamp2Name + ".color", 1, 0, 0, type="double3")
    
    
    #we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp2, aimVector= (0, 0, -1))
    
def nouveau():
     
    #save the selection
    myModel = cmds.ls( sl=True) 
    
    #we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)
    
    #light Top Left
    lamp1Name = cmds.directionalLight(intensity=1)
    cmds.move(bb[0], bb[4]*0.60, bb[5])
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 0)
    
    
    #light RED filler Bottom Right
    lamp2Name = cmds.directionalLight(intensity=1)
    cmds.move(bb[0]*0.094, bb[1]/0.698, bb[5])
    lamp2 = cmds.ls( sl=True)
    cmds.setAttr(lamp2Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp2Name + ".aiAngle", 92.169)
    cmds.setAttr(lamp2Name + ".color",0.738, 0.255, 0.177, type ="double3")
    
 #light bougie centerleft
    lamp3Name = cmds.directionalLight(intensity=1)
    cmds.move(bb[0], bb[4]*0.40, bb[5])
    lamp3 = cmds.ls( sl=True)
    cmds.setAttr(lamp3Name + ".aiShadowDensity",0.05 ) 
    cmds.setAttr(lamp3Name + ".color",1, 0.584, 0.314, type ="double3")
   
    #we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp2, aimVector= (0, 0, -1))
    cmds.aimConstraint(myModel, lamp3, aimVector= (0, 0, -1))


def gant():
    
    #save the selection
    myModel = cmds.ls( sl=True) 
    
    #we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)

    #light Top Left
    lamp1Name = cmds.directionalLight(intensity=3)
    cmds.move(bb[0], bb[4]*0.9, bb[5]*0.08)
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.5 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 45)
    cmds.setAttr(lamp1Name + ".color",2.154, 1.768, 0.936, type ="double3")
       
   
    #we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    
    

def ferronniere():
    
    #save the selection
    myModel = cmds.ls( sl=True) 
    
    #we get the bounding box
    # xmin ymin zmin xmax ymax zmax
    #[ 0  ,  1,   2,   3,   4,   5]
    bb = cmds.xform(q=True, bb=True)

    #light Top Left
    lamp1Name = cmds.directionalLight(intensity=2.5)
    cmds.move(bb[0]/1.8, bb[4]/1.2, bb[5])
    lamp1 = cmds.ls( sl=True)
    cmds.setAttr(lamp1Name + ".aiShadowDensity",0.0005 ) 
    cmds.setAttr(lamp1Name + ".aiAngle", 45)
    cmds.setAttr(lamp1Name + ".color",0.757, 0.721, 0.520, type ="double3")
       
   
    #we aim the lights at the model
    cmds.aimConstraint(myModel, lamp1, aimVector= (0, 0, -1))
    
    
    
def spleenEtIdeal():
    
    MyModel = cmds.ls (sl = True)
    
    bb = cmds.xform (q = True, bb = True)
    
    # Yellow Directionnal Light at top left 
    yellowLamp = cmds.directionalLight (n='Yellow_directionalLight') # creer light
    cmds.setAttr(yellowLamp + '.color', 1, 0.3797, 0, type = 'double3') # couleur
    cmds.setAttr(yellowLamp + '.intensity', 5.0) # intensite
    cmds.rotate(126.18, -70.894, -143.975, yellowLamp)# rotate 
    cmds.move(bb[0]-30.0,bb[4]+46.0,bb[5]+36.0) # move

    # Pink Directional Light at top left
    pinkLamp = cmds.directionalLight (n='Pink_directionalLight')
    cmds.setAttr(pinkLamp + '.color', 0.331, 0.126, 0.089, type = 'double3') 
    cmds.setAttr(pinkLamp + '.intensity', 20.0)  
    cmds.rotate(126.18, -70.894, -143.975, pinkLamp) 
    cmds.move(bb[0]-30.0,bb[4]+40.0,bb[5]+30.0)
    
    # Blue Directional Light at top right
    blueLamp = cmds.directionalLight (n='Blue_directionalLight')
    cmds.setAttr(blueLamp + '.color', 0.263, 0.263, 1, type = 'double3')
    cmds.setAttr(blueLamp + '.intensity',1.0) 
    cmds.rotate(35.574, 35.533, 97.83, blueLamp)
    cmds.move(bb[3]+11.0,bb[4]+41.0,bb[5]+41.0)

    # Area Light in top front
    whiteLamp = cmds.shadingNode('areaLight', asLight = True)
    cmds.setAttr(whiteLamp + '.color', 1, 0.922, 0.788, type = 'double3')
    cmds.rotate(-32.6, 0, 0, whiteLamp)
    cmds.move((bb[3]+bb[0])/2, bb[4], ((bb[5]+bb[2])/2)+50)



# Delete all lights in scene
 
def DeleteAllLights():    
    AllLights = cmds.ls(lights=True)
    # print(AllLights)
    cmds.delete([cmds.listRelatives(lamp, parent=True)[0] for lamp in AllLights])
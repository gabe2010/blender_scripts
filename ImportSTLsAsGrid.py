import bpy
import os
import math
import random

directory = os.path.dirname(bpy.data.filepath)

path = directory + "//STLs"

print(path)

gridsize = 80

gridx = 5
gridy = 5

i = 0 

def importStls(i):
    for stl in os.listdir(path):
        stlpath = path+"//"+stl
        print(stlpath)
        
        xOffset = gridsize * (i%gridx)
        yOffset = gridsize * math.trunc(i / gridy)
    
        zRot = random.uniform(-180,180)
    
        bpy.ops.import_mesh.stl(filepath=stlpath)
        bpy.ops.transform.translate(value=(xOffset, yOffset, 0))
        bpy.ops.transform.rotate(value=zRot, orient_axis='Z')
    
        i += 1


#make all objects same mat
def setMat():
    for obj in bpy.data.objects:
        if obj.type == "MESH" and obj.name != "Table":
            print(obj.name)
            obj.active_material = bpy.data.materials["CrispMatYellow"]


importStls(i)
setMat()


import bpy
import os
folder = "C://Workspaces//GabeServerPC//OssOss//Mocap//STATE_001"

arm = bpy.data.objects["Skeleton"]

cloth = bpy.data.objects["Plane"]

bScaleAnims = False

def Select(obj):
    #bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    
def DeselectAll():
    bpy.ops.object.select_all(action='DESELECT')
    
def importBvh(dir):
    for bvh in os.listdir(dir):
        print(bvh)
        path = (dir+"//"+bvh)
        print(path)
        bpy.ops.import_anim.bvh(filepath=(path))
        
        
    #Load BVH file into action strip

for action in bpy.data.actions:
    Select(arm)
    arm.animation_data.action=(action)

    #Scale BVH action by 0.2 relative to the first frame
    if bScaleAnims == True:
        bpy.context.area.type = "DOPESHEET_EDITOR"
        bpy.ops.transform.transform(mode='TIME_SCALE', value=(0.2, 0, 0, 0), orient_axis='Z', orient_type='VIEW', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    #Get animation length
    LastFrame = action.frame_range[1]
    print(LastFrame)
    
    #Make an new Cache
    Select(cloth)
    bpy.context.area.type= "PROPERTIES"
    bl_region_type = "WINDOW"
    bpy.context.space_data.context = 'PHYSICS'

    bpy.ops.ptcache.add()
    bpy.context.area.type= "TEXT_EDITOR"
    bpy.context.object.modifiers["Cloth"].point_cache.name = action.name

    #Set Cache bake end time
    
    #Set New Cache name to BVH file name
    
    #Bake Cache 
    
    #https://blenderartists.org/t/how-to-use-bpy-ops-ptcache-bake-from-cache/540926/13
    
    #https://docs.blender.org/api/current/bpy.ops.ptcache.html
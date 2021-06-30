#--------Creates a bone for object in the scene, adds constraints to each bone
#        then makes a copy of all objects as one new object and binds it to the armature

#        Used for baking physics simulations for use in UE

import bpy
import mathutils

bpy.ops.object.armature_add(location=(0, 0, 0))

NewArmName = "PhysArmature"
NewMeshName = "NewMesh"
bpy.context.object.name = NewArmName
armature = bpy.data.objects[NewArmName]


for obj in bpy.data.objects:
    if obj.hide_get() == False:
        if obj.type == 'MESH':
            NewName = obj.name
            
            #Make and Assign Vertex Group
            group = obj.vertex_groups.new(name = obj.name)
            i = 0
            for v in obj.data.vertices:
                group.add([i], 1, 'REPLACE')
                i += 1
            
            # must be in edit mode to add bones
            bpy.context.view_layer.objects.active = armature
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            edit_bones = armature.data.edit_bones

            b = edit_bones.new(obj.name)
            # a new bone will have zero length and not be kept
            
            v = mathutils.Vector((0,0,1))#define rotation of new bone
            b.head = (obj.location)# move the head
            b.tail = (obj.location + v)# move the tail
            bpy.ops.object.editmode_toggle()
            
            constraints = armature.pose.bones[(NewName)].constraints
                  
            constraints.new(type='COPY_ROTATION').target = obj
            constraints["Copy Rotation"].mix_mode = 'ADD'
            constraints.new(type='COPY_LOCATION').target = obj
            
#Select All Meshes
for ob in bpy.context.scene.objects:
    if ob.hide_get() == False:
        if ob.type == 'MESH':
            ob.select_set(state = True)
            bpy.context.view_layer.objects.active = ob
        else:
            ob.select_set  (state = False)
#Make a copy
bpy.ops.object.duplicate()

#Join
bpy.ops.object.join()
bpy.context.object.name = NewMeshName
bpy.context.scene.cursor.location = (armature.location)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

      

bpy.context.view_layer.objects.active = armature #Make Armature Active
bpy.ops.object.parent_set(type='ARMATURE', xmirror=False, keep_transform=False)

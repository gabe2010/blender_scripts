#------- Adds a bone per vertex of an object, adds constraints
#        makes new copy of object and bakes animation

#        used for baking cloth animations for use in UE

import bpy, mathutils

mesh = bpy.data.objects["Plane"]

userot = False

NewArmName = "PhysArmature"
NewObjName = "NewObj"
bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(mesh.location), scale=(1, 1, 1))
bpy.context.object.name = NewArmName
armature = bpy.data.objects[NewArmName]

i = 0
offset = mathutils.Vector((0,0,0.5))#define rotation of new bone

for v in mesh.data.vertices:
    edit_bones = armature.data.edit_bones

    bone_name = f"{i}"
    print (bone_name)
    bone = edit_bones.new(bone_name)
    
    # a new bone will have zero length and not be kept        
    bone.head = (v.co)# move the head
    bone.tail = (v.co + offset)# move the tail
    
    bpy.ops.object.editmode_toggle()

    #make a new vertex group and assign current vertex
    group = mesh.vertex_groups.new(name = bone_name)
    group.add([i], 1, 'REPLACE')
    i += 1
    
    #MakeConstraints
    constraints = armature.pose.bones[(bone_name)].constraints
    if userot == True:                  
        constraints.new(type='COPY_ROTATION').target = mesh
        constraints["Copy Rotation"].mix_mode = 'ADD'
        constraints["Copy Rotation"].subtarget = bone_name #assign target vertex group
    constraints.new(type='COPY_LOCATION').target = mesh
    constraints["Copy Location"].subtarget = bone_name #assign target vertex group
    bpy.ops.object.editmode_toggle()
    

armature.select_set(state = False)

bpy.ops.object.mode_set(mode='OBJECT', toggle=True)
bpy.context.view_layer.objects.active = mesh
mesh.select_set(state = True)
bpy.ops.object.duplicate_move()
bpy.context.object.name = NewObjName
bpy.ops.object.modifier_remove(modifier="Cloth")


bpy.context.view_layer.objects.active = armature #Make Armature Active
bpy.ops.object.parent_set(type='ARMATURE', xmirror=False, keep_transform=False)
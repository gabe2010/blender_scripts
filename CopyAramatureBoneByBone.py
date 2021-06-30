#-------Copys all bone transforms to duplicate armature.
#       used for baking spline IK actions to animations for export to UE4
#       Note! works well in blender without, but Deform Arm bones should be unparented from one another for consistent use un UE


import bpy
D= bpy.data;


DeformArm = D.objects["DeformArmature"];

SplineArm = D.objects["SplineIKArmature"];

for bone in DeformArm.data.bones:
    print (bone.name);
    bone.inherit_scale = 'NONE';
    
    #Add constriant:
    NewConstraint = DeformArm.pose.bones[(bone.name)].constraints.new(type='COPY_TRANSFORMS');
    print  (NewConstraint.name);
    NewConstraint.target = SplineArm;
    NewConstraint.subtarget = bone.name;

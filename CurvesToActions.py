#--------Iterates through all Curves ina a scene, Constrains Spline IK Armature to them then copies post to Deform Armature
#        Used for making a library of poses from SVG curves for use in UE4
import bpy

DeformArm = bpy.data.objects["DeformArmature"];
SplineArm = bpy.data.objects["SplineIKArmature"];


def Select(obj):
    #bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    
def SetSockets(obj):
    #First make the constraint
    SocConstraint = DeformArm.pose.bones["Socket"].constraints.new(type='COPY_LOCATION');
    OrConstraint = DeformArm.pose.bones["Origin"].constraints.new(type='COPY_LOCATION');
    #Set Target
    SocConstraint.target = bpy.data.objects[str("{0}_Socket".format(obj.name))]
    OrConstraint.target = bpy.data.objects[str("{0}_Origin".format(obj.name))]   
              
                
def LinkCurve(obj):
    Select(SplineArm)
    bpy.context.object.pose.bones["Bone.099"].constraints["Spline IK"].target = obj
    
    
        
    bpy.ops.object.select_all(action='DESELECT')
    
def BakeAnim(name):
    Select(DeformArm)
    bpy.ops.nla.bake(frame_start=1, frame_end=1, only_selected=False, clear_constraints=True, visual_keying=True, bake_types={'POSE'})
    bpy.data.actions["Action"].name = name
    
    
def AddCopyConstraints():
    for bone in DeformArm.data.bones:
        #print (bone.name);
        bone.inherit_scale = 'NONE';
    
        #Add constriant:
        if (bone.name != "Socket") and (bone.name != "Origin"):
            NewConstraint = DeformArm.pose.bones[(bone.name)].constraints.new(type='COPY_TRANSFORMS');
            NewConstraint.target = SplineArm;
            NewConstraint.subtarget = bone.name;
    
    #Add Socket and Origin Constraints Manually
        
    
index = 0
for Curve in bpy.data.objects:
    if Curve.type == "CURVE":
        if index < 1000:
            LinkCurve(Curve)   
            SetSockets(Curve) 
            AddCopyConstraints()
            BakeAnim(Curve.name)
            bpy.ops.object.select_all(action='DESELECT')
            index += 1




    
    


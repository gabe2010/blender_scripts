#---------- Adds 2 empties per curve in scene and parents them to the Curve

import bpy

s = 0.005;
s3 = (s, s, s);

def MakeOrigin(curve):
    loc = curve.data.splines[0].bezier_points[0].co;
    Name = ("{0}_Origin").format(curve.name);
    bpy.ops.object.empty_add(type='CIRCLE');
    newobj = bpy.context.active_object;
    newobj.name= Name;
    newobj.rotation_euler[0] = 1.5708;
    newobj.parent =  curve;
    newobj.scale = s3;
    newobj.location = loc;
    
    bpy.ops.collection.objects_remove_all()
    bpy.data.collections['Letters'].objects.link(newobj)
    return;
    
def MakeSocket(curve):
    lastpointindex = len(curve.data.splines[0].bezier_points);
    loc = curve.data.splines[0].bezier_points[lastpointindex-1].co;
    
    Name = ("{0}_Socket").format(curve.name);
    bpy.ops.object.empty_add(type='CUBE');
    newobj = bpy.context.active_object;
    newobj.name = Name;
    
    newobj.parent =  curve;
    newobj.scale = s3;
    newobj.location = loc;
    
    bpy.ops.collection.objects_remove_all()
    bpy.data.collections['Letters'].objects.link(newobj)
    return;
    
for curve in bpy.data.objects:
    if curve.type =="CURVE":
        
        MakeOrigin(curve);
        MakeSocket(curve);
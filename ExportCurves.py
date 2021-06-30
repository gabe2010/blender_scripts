#------ Writes a CSV file for import into UE4 as a data table of all curves in the scene.

#Last used in blender 2.92

import bpy
from os import listdir
from os.path import isfile, join
from mathutils import Vector

D = bpy.data;
dec = 8; ##Number of Decimalplaces for curve Locations + 2

def FormatVector(Vector):
    x = Vector[0];
    y = Vector[1];
    z = Vector[2];
    
    s = str("(X={0},Y={1},Z={2})").format(str(x)[:dec], str(z)[:dec], str(y)[:dec]);
    ##s = str("X="+(Vector[0])+", Y="+str(Vector[1])+", Z="+str(Vector[2]));
    return s;

## Create txt file

File = open("C://Users//gabe//Desktop//Curves03.csv", "w");

File.write("---,Letters\n");

CurrentLetter = "";
LetterIndex = 1;

#For Each Curve in Scene:


Letters = [];
for Curve in D.objects:
    if Curve.type == "CURVE":
        Letters.append(Curve);
        
for Letter in Letters: ## For Curves in Scene in sub directory   
    #New Row
    if Letter.name[0] != CurrentLetter:
        if CurrentLetter != "":
            File.write('))"');
            File.write("\n");
        CurrentLetter = Letter.name[0];
        
        
        File.write(CurrentLetter+',"('); ##Write Name Of Letter
        LetterIndex = 1;
    else:
        LetterIndex += 1;
        File.write('),');
        
    
    ##LetterName = CurrentLetter+str(LetterIndex).zfill(2);
    File.write('(Name=""{0}"",Points=('.format(Letter.name));

    #Loop Through Points in Curve
    for spline in Letter.data.splines:
        PointIndex = 0;
        ##Get location, Handle location 01, Handle location 02
        for point in spline.bezier_points:
            ##Write To File
            point.handle_left_type = "VECTOR";
            point.handle_right_type = "VECTOR";
            point.handle_left_type = "ALIGNED";
            point.handle_right_type = "ALIGNED";
            File.write("(");
            File.write("Pos="+FormatVector(point.co));
            File.write(",ArriveTangent="+FormatVector(point.handle_left));
            File.write(",LeaveTangent="+FormatVector(point.handle_right)); 
            File.write(")");
            if (PointIndex < len(spline.bezier_points)-1):
                File.write(",");
            PointIndex += 1;
    File.write(")");   
File.close();

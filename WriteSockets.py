#--------- Writes a .CSV for import of data into UE of "Sockets and Origins" - empties for reference -
import bpy

dec = 8; ##Number of Decimalplaces for curve Locations + 2

def FormatVector(Vector):
    x = Vector[0];
    y = Vector[1];
    z = Vector[2];
    
    s = str("(X={0},Y=0,Z={1})").format(str(x)[:dec], str(y)[:dec]);
    ##s = str("X="+(Vector[0])+", Y="+str(Vector[1])+", Z="+str(Vector[2]));
    return s;

D = bpy.data;

File = open("D://Desktop//Sockets02.csv", "w");

File.write("---,Curve");

Letters = [];
for Curve in D.objects:
    if Curve.type == "CURVE":
        Letters.append(Curve);
        
        
print("New:");

CurrentLetter = "";
index = 0;
for Letter in Letters:
    Name = Letter.name;
    if Name[0] != CurrentLetter:
        CurrentLetter = Name[0];
        if index != 0:
            ##Close Previous Letters' Parenthasis
            File.write(')"');     
        File.write("\n");
        File.write(str('{0},"(').format(Name[0]));
        index += 1;
    elif len(Letter.children) != 0:
        File.write(',');

    for Child in Letter.children:
        if Child.empty_display_type == "CIRCLE":
            File.write(str('(Origin={0}').format(FormatVector(Child.location)));

       
    for Child in Letter.children:
        if Child.empty_display_type == "CUBE":
            File.write(str(',Socket={0})').format(FormatVector(Child.location)));

    
    
        
##Close Last Letters' Parenthasis
File.write(')"');

    
##Close File
File.close();
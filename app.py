"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)

# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"


"""
██████╗ ██████╗ ██╗██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝ ██╔════╝
██████╔╝██████╔╝██║██║  ██║██║  ███╗█████╗  
██╔══██╗██╔══██╗██║██║  ██║██║   ██║██╔══╝  
██████╔╝██║  ██║██║██████╔╝╚██████╔╝███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝ ╚══════╝
"""           
## Import necessary libraries
import rhino3dm

#create a complex trigonometric polynomial that defines the surface of a architectural bridge design with the @hops component decorator
#write this into a @hops component
@hops.component(
    "/drawbridge_04",
    name="Drawbridge",
    description="Create a drawbridge",
    inputs=[
        hs.HopsInteger("Length", "L", "Length of the drawbridge"),
        hs.HopsInteger("Width", "W", "Width of the drawbridge"),
        hs.HopsInteger("Height", "H", "Height of the drawbridge")
    ],
    outputs=[
        hs.HopsCurve("Base", "B", "Base of the drawbridge")
    ]
)
def drawbridge_04(length, width, height):
    #start with points at the corners of the bridge
    pt1 = rhino3dm.Point3d(0, 0, 0)
    pt2 = rhino3dm.Point3d(length, 0, 0)
    pt3 = rhino3dm.Point3d(length, width, 0)
    pt4 = rhino3dm.Point3d(0, width, 0)

    #create a curve from the points
    base = rhino3dm.Curve.CreateControlPointCurve([pt1, pt2, pt3, pt4], 1)

    return base

#create a complex trigonometric polynomial that defines the surface of a architectural bridge design 
#with more architecture like a drawbridge
# with the @hops component decorator
#write this into a @hops component
@hops.component(
    "/drawbridge_07",
    name="Drawbridge",
    description="Create a drawbridge",
    inputs=[
        hs.HopsInteger("Length", "L", "Length of the drawbridge"),
        hs.HopsInteger("Width", "W", "Width of the drawbridge"),
        hs.HopsInteger("Height", "H", "Height of the drawbridge"),
        hs.HopsInteger("Degree", "D", "Degree of the drawbridge")
    ],  
    outputs=[
        hs.HopsCurve("Base", "B", "Base of the drawbridge"),
        hs.HopsCurve("Top", "T", "Top of the drawbridge")
    ]
)
def drawbridge_07(length, width, height, degree):
    #start with points at the corners of the bridge
    points = []
    pt1 = rhino3dm.Point3d(0, 0, 0)
    pt2 = rhino3dm.Point3d(length, 0, 0)
    pt3 = rhino3dm.Point3d(length, width, 0)
    pt4 = rhino3dm.Point3d(0, width, 0)
    #add the points to the list
    points.append(pt1)
    points.append(pt2)
    points.append(pt3)
    points.append(pt4)


    #create a curve from the points
    base = rhino3dm.Curve.CreateControlPointCurve([pt1, pt2, pt3, pt4], 1)

    #create a second curve that is offset from the first with a rhino3dm function
    offset = base.CreateControlPointCurve(points, degree)

    return base, offset

#create a complex trigonometric polynomial that defines the surface of a architectural bridge design 
#with more architecture like a drawbridge
#and rotate the bridge so it goes up and down
# with the @hops component decorator
#write this into a @hops component
@hops.component(
    "/drawbridge_10",
    name="Drawbridge",
    description="Create a drawbridge",
    inputs=[
        hs.HopsNumber("Length", "L", "Length of the drawbridge"),  
        hs.HopsNumber("Width", "W", "Width of the drawbridge"),
        hs.HopsNumber("Height", "H", "Height of the drawbridge"),
        hs.HopsInteger("Degree", "D", "Degree of the drawbridge"),
        hs.HopsNumber("Angle", "A", "Angle of the drawbridge")
    ],
    outputs=[
        hs.HopsCurve("Base", "B", "Base of the drawbridge"),
        hs.HopsCurve("Top", "T", "Top of the drawbridge")
    ]
)
def drawbridge_10(length, width, height, degree, angle):
    #start with points at the corners of the bridge
    points = []
    pt1 = rhino3dm.Point3d(0, 0, 0)
    pt2 = rhino3dm.Point3d(length, 0, 0)
    pt3 = rhino3dm.Point3d(length, width, 0)
    pt4 = rhino3dm.Point3d(0, width, 0)
    #add the points to the list
    points.append(pt1)
    points.append(pt2)
    points.append(pt3)
    points.append(pt4)


    #create a curve from the points
    base = rhino3dm.Curve.CreateControlPointCurve([pt1, pt2, pt3, pt4], 1)

    #create a second curve that is offset from the first with a rhino3dm function
    offset = base.CreateControlPointCurve(points, degree)

    #rotate the bridge
    offset.Rotate(angle, rhino3dm.Vector3d(0, 1, 0), rhino3dm.Point3d(0, 0, 0))

    return base, offset

#create a complex trigonometric polynomial that defines the surface of a architectural bridge design 
#with more architecture like a drawbridge
#and rotate the bridge so it goes up and down
#and create a vertical doorway for the drawbridge when it is up
# with the @hops component decorator
#write this into a @hops component
@hops.component(
    "/drawbridge_15",
    name="Drawbridge",
    description="Create a drawbridge",
    inputs=[
        hs.HopsNumber("Length", "L", "Length of the drawbridge"),
        hs.HopsNumber("Width", "W", "Width of the drawbridge"),
        hs.HopsNumber("Height", "H", "Height of the drawbridge"),
        hs.HopsInteger("Degree", "D", "Degree of the drawbridge"),
        hs.HopsNumber("Angle", "A", "Angle of the drawbridge"),
        hs.HopsNumber("Door Height", "DH", "Height of the door")
    ],
    outputs=[
        hs.HopsCurve("Base", "B", "Base of the drawbridge"),
        hs.HopsCurve("Top", "T", "Top of the drawbridge"),
        hs.HopsCurve("Door", "D", "Door of the drawbridge")
    ]
)
def drawbridge_15(length, width, height, degree, angle, door_height):
    #start with points at the corners of the bridge
    points = []
    pt1 = rhino3dm.Point3d(0, 0, 0)
    pt2 = rhino3dm.Point3d(length, 0, 0)
    pt3 = rhino3dm.Point3d(length, width, 0)
    pt4 = rhino3dm.Point3d(0, width, 0)
    #add the points to the list
    points.append(pt1)
    points.append(pt2)
    points.append(pt3)
    points.append(pt4)


    #create a curve from the points
    base = rhino3dm.Curve.CreateControlPointCurve([pt1, pt2, pt3, pt4], 1)

    #create a second curve that is offset from the first with a rhino3dm function
    offset = base.CreateControlPointCurve(points, degree)

    #rotate the bridge
    offset.Rotate(angle, rhino3dm.Vector3d(0, 1, 0), rhino3dm.Point3d(0, 0, 0))

    #create a door frame for the drawbridge as a vertical rectangle
    door = rhino3dm.Curve.CreateControlPointCurve([rhino3dm.Point3d(0, 0, 0), rhino3dm.Point3d(0, 0, door_height), rhino3dm.Point3d(0, width, door_height), rhino3dm.Point3d(0, width, 0)], 1)

    return base, offset, door

"""
██████╗ ██████╗ ██╗██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝ ██╔════╝
██████╔╝██████╔╝██║██║  ██║██║  ███╗█████╗  
██╔══██╗██╔══██╗██║██║  ██║██║   ██║██╔══╝  
██████╔╝██║  ██║██║██████╔╝╚██████╔╝███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                            
██████╗  █████╗ ██████╗ ████████╗    ██╗██╗ 
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║██║ 
██████╔╝███████║██████╔╝   ██║       ██║██║ 
██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║██║ 
██║     ██║  ██║██║  ██║   ██║       ██║██║ 
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚═╝ 
"""
import Rhino
import math
import scriptcontext
import rhinoscriptsyntax as rs

def create_cylinder_bridge(length, width, height, divisions, pillar_radius, beam_radius, road_thickness, railing_height, railing_thickness):
    # Calculate division length
    div_length = length / divisions
    
    # Initialize list for bridge components
    bridge = []
    
    # Create cylinders for the bridge
    for i in range(divisions):
        x = i * div_length
        base_point = Rhino.Geometry.Point3d(x, width/2, 0)
        
        # Create cylinder
        base_circle = Rhino.Geometry.Circle(base_point, pillar_radius)
        cylinder = Rhino.Geometry.Cylinder(base_circle, height)
        
        # Add cylinder to bridge
        bridge.append(cylinder.ToBrep(True, True))

        # If it's not the first or last division, create the beam between pillars
        if i > 0:
            start_point = Rhino.Geometry.Point3d(x - div_length, width/2, height)
            end_point = Rhino.Geometry.Point3d(x, width/2, height)
            line = Rhino.Geometry.Line(start_point, end_point)

            # Calculate midpoint of the line
            midpoint = Rhino.Geometry.Point3d((start_point.X + end_point.X) / 2, (start_point.Y + end_point.Y) / 2, (start_point.Z + end_point.Z) / 2)

            beam = Rhino.Geometry.Cylinder(Rhino.Geometry.Circle(midpoint, beam_radius), line.Length)
            
            # Add beam to bridge
            bridge.append(beam.ToBrep(True, True))
    
    # Create the road on the top of the pillars
    road_height = height + road_thickness
    road_base = Rhino.Geometry.Point3d(0, 0, height)
    road_points = [
        Rhino.Geometry.Point3d(road_base[0], road_base[1], road_base[2]),
        Rhino.Geometry.Point3d(road_base[0] + length, road_base[1], road_base[2]),
        Rhino.Geometry.Point3d(road_base[0] + length, road_base[1] + width, road_base[2]),
        Rhino.Geometry.Point3d(road_base[0], road_base[1] + width, road_base[2]),
        Rhino.Geometry.Point3d(road_base[0], road_base[1], road_base[2] + road_thickness),
        Rhino.Geometry.Point3d(road_base[0] + length, road_base[1], road_base[2] + road_thickness),
        Rhino.Geometry.Point3d(road_base[0] + length, road_base[1] + width, road_base[2] + road_thickness),
        Rhino.Geometry.Point3d(road_base[0], road_base[1] + width, road_base[2] + road_thickness),
    ]

    # Create road
    road = Rhino.Geometry.Brep.CreateFromBox(road_points)
    
    # Add road to bridge
    bridge.append(road)

    # Create railings
    railing_base_height = height + road_thickness
    railing_top_height = railing_base_height + railing_height

    # Left railing
    left_railing_start = Rhino.Geometry.Point3d(0, railing_thickness / 2, railing_base_height)
    left_railing_end = Rhino.Geometry.Point3d(length, railing_thickness / 2, railing_base_height)
    left_railing_line = Rhino.Geometry.Line(left_railing_start, left_railing_end)
    left_railing_midpoint = left_railing_line.PointAt(0.5)
    left_railing = Rhino.Geometry.Cylinder(Rhino.Geometry.Circle(left_railing_midpoint, railing_thickness / 2), railing_height)
    bridge.append(left_railing.ToBrep(True, True))
    
    # Right railing
    right_railing_start = Rhino.Geometry.Point3d(0, width - railing_thickness / 2, railing_base_height)
    right_railing_end = Rhino.Geometry.Point3d(length, width - railing_thickness / 2, railing_base_height)
    right_railing_line = Rhino.Geometry.Line(right_railing_start, right_railing_end)
    right_railing_midpoint = right_railing_line.PointAt(0.5)
    right_railing = Rhino.Geometry.Cylinder(Rhino.Geometry.Circle(right_railing_midpoint, railing_thickness / 2), railing_height)
    bridge.append(right_railing.ToBrep(True, True))

    # Define number of railing segments
    railing_segments = 10
    
    # Calculate the length of each segment
    segment_length = length / railing_segments
    
    # Create railings
    for i in range(railing_segments):
        x = i * segment_length
        
        # Left railing
        left_railing_start = Rhino.Geometry.Point3d(x, railing_thickness / 2, railing_base_height)
        left_railing_end = Rhino.Geometry.Point3d(x + segment_length, railing_thickness / 2, railing_base_height)
        left_railing_line = Rhino.Geometry.Line(left_railing_start, left_railing_end)
        left_railing_midpoint = left_railing_line.PointAt(0.5)
        left_railing = Rhino.Geometry.Cylinder(Rhino.Geometry.Circle(left_railing_midpoint, railing_thickness / 2), railing_height)
        bridge.append(left_railing.ToBrep(True, True))
        
        # Right railing
        right_railing_start = Rhino.Geometry.Point3d(x, width - railing_thickness / 2, railing_base_height)
        right_railing_end = Rhino.Geometry.Point3d(x + segment_length, width - railing_thickness / 2, railing_base_height)
        right_railing_line = Rhino.Geometry.Line(right_railing_start, right_railing_end)
        right_railing_midpoint = right_railing_line.PointAt(0.5)
        right_railing = Rhino.Geometry.Cylinder(Rhino.Geometry.Circle(right_railing_midpoint, railing_thickness / 2), railing_height)
        bridge.append(right_railing.ToBrep(True, True))
"""
    import numpy as np
    
    # Create catenary arch cables
    for i in range(divisions - 1):
        x_start = i * div_length
        x_end = (i + 1) * div_length
    
        start_point = Rhino.Geometry.Point3d(x_start, width / 2, height + road_thickness)
        end_point = Rhino.Geometry.Point3d(x_end, width / 2, height + road_thickness)
    
        # Define the catenary scale (adjust this to get desired catenary shape)
        a = 5  # arbitrary value
    
        # Define number of points for each catenary
        num_points = 100
    
        # Create the points for the catenary curve
        x_values = np.linspace(x_start, x_end, num_points)
        y_values = a * np.cosh((x_values - (x_start + x_end) / 2) / a) - a + height + road_thickness
        catenary_points = [Rhino.Geometry.Point3d(x, width / 2, y) for x, y in zip(x_values, y_values)]
    
        # Create the catenary curve
        catenary_curve = Rhino.Geometry.Curve.CreateInterpolatedCurve(catenary_points, 3)
    
        # Add curve to bridge
        bridge.append(catenary_curve.ToNurbsCurve())

    # Return bridge components
    return bridge

# Create a cylinder bridge with railings
bridge = create_cylinder_bridge(length, width, height, divisions, pillar_radius, beam_radius, road_thickness, railing_height, railing_thickness)

# Output the bridge
a = bridge
"""

#pip install rhino3dm
#pip install compute-rhino3d

import rhino3dm
import random
import compute_rhino3d.Util
import compute_rhino3d.Curve

model = rhino3dm.File3dm()

compute_rhino3d.Util.authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjoiUEtDUyM3IiwiYyI6IkFFU18yNTZfQ0JDIiwiYjY0aXYiOiJxTmRUWVU4bEFJMGJ3ZkNFOWI4UjV3PT0iLCJiNjRjdCI6InFMYmZwaFFXMnFkbWI2MDdydURQM2VVMmNpQVpwSDVPWGlzNGtReXFNUEo5UFF1T1crRmZZRTRZSDYwQWk2bVNZaHpQNUY2RllSai9yRm9uNUFWUnFBODUxL0lqNktsTWdlWFl4T3RyTjAwNjFSeEpiS0lnYnlZakY0dFpJZnl1Qlk5SmErb1JMa3prY3RBeWk1WVVMWGFBR3NueVpGSStJbmg3Y205UC8yd0ZYdWJjUnVmeElUdlNTSVoyOWtUZlJGYXdkNVp2OE1nRnRZU0FTbmpoT3c9PSIsImlhdCI6MTY4Njk1MDQyMX0.kKdNMqWc7msCCxGHxoOGS4LqqomnZK6H23vj0h_n4tE"

curves = []

for i in range(20):
    pt = rhino3dm.Point3d(random.uniform(-10, 10), random.uniform(-10, 10), 0)
    circle = rhino3dm.Circle(pt, random.uniform(1, 4))
    curve = circle.ToNurbsCurve()
    curves.append(curve)

#create a compute_rhino3d point3d object
bcurves = compute_rhino3d.Curve.CreateBooleanUnion(curves)



"""
#create a compute_rhino3d.Curve.CreateBooleanUnion 
bcurves = compute_rhino3d.Curve.CreateBooleanUnion(curves)

for bcurve in bcurves:
    #bcurveObj = rhino3dm.CommonObject.Decode(bcurve)
    model.Objects.AddCurve(bcurve)
"""

model.Write('boolean2d.3dm', 6)




if __name__ == "__main__":
    app.run(debug=True)
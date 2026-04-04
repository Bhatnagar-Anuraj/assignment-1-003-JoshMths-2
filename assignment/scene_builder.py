"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
# tower base dimensions
tower_base_radius = 3
tower_base_height = 7
tower_base_x = 6
tower_base_z = 3

# create tower base 
tower_base = cmds.polyCylinder(
name = "Water Tower Base",
radius = tower_base_radius,
height = tower_base_height,
)[0]

# move tower base and position above plane
cmds.move(tower_base_x, tower_base_height/2 , tower_base_z, tower_base)

# ---------------------------------------------------------------------------
# TODO: Add Object 3
# ---------------------------------------------------------------------------
# tower top dimensions
W_tower_top_width = 5
W_tower_top_height = 5
W_tower_top_depth = 5
W_tower_top_x = 6
W_tower_top_z = 3

# create tower top
W_tower_top = cmds.polyCube(
name = "Water Tower Top",
width = W_tower_top_width,
height = W_tower_top_height,
depth = W_tower_top_depth,
)[0]

# move tower top and position above tower base
cmds.move(W_tower_top_x, W_tower_top_height/2 + 7 , W_tower_top_z, W_tower_top)
 

# ---------------------------------------------------------------------------
# TODO: Add Object 4
# ---------------------------------------------------------------------------
# church base dimensions
church_b_width = 4
church_b_height = 6
church_b_depth = 5
church_b_x = -4
church_b_z = -5

# create church base
church_b = cmds.polyCube(
name = "Church Base",
width = church_b_width,
height = church_b_height,
depth = church_b_depth,
)[0]

# move church base and position above plane
cmds.move(church_b_x, church_b_height/2, church_b_z, church_b) 

# ---------------------------------------------------------------------------
# TODO: Add Object 5
# ---------------------------------------------------------------------------
# church top dimensions
church_t_radius = 4
church_t_height = 5
church_t_x = -4
church_t_z = -5

# create church top
church_t = cmds.polyCone(
name = "Church Top",
radius = church_t_radius,
height = church_t_height,
)[0]

# move church top and position right above church base
cmds.move(church_t_x, church_t_height/2 + 6, church_t_z, church_t)

# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")

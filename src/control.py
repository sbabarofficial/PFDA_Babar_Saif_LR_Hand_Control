import maya.cmds as cmds

def create_cube_control(name, size, position):

    ctrl = cmds.curve(
        name=name,
        d=1,
        p=[
            (-size, -size, -size),
            (-size, -size, size),
            (-size, size, size),
            (-size, size, -size),
            (-size, -size, -size),
            (size, -size, -size),
            (size, -size, size),
            (-size, -size, size),
            (-size, size, size),
            (size, size, size),
            (size, -size, size),
            (size, -size, -size),
            (size, size, -size),
            (-size, size, -size),
            (-size, size, size),
            (size, size, size),
            (size, size, -size)
        ]
    )

    grp = cmds.group(ctrl, name=f"{name}_grp")

    cmds.xform(grp, ws=True, t=position)

    cmds.makeIdentity(grp, apply=True, t=True, r=True, s=True)

    return ctrl, grp


def mirror_control(control):

    
    grp = cmds.listRelatives(control, parent=True)[0]

    
    pos = cmds.xform(grp, q=True, ws=True, t=True)
    x, y, z = pos

    #
    axis_values = {"X": abs(x), "Y": abs(y), "Z": abs(z)}
    mirror_axis = max(axis_values, key=axis_values.get)

    
    dup_grp = cmds.duplicate(grp)[0]

    
    dup_ctrl = cmds.listRelatives(dup_grp, children=True)[0]

    
    if control.startswith("L_"):
        new_name = dup_ctrl.replace("L_", "R_")
    elif control.startswith("R_"):
        new_name = dup_ctrl.replace("R_", "L_")
    else:
        new_name = dup_ctrl

    dup_ctrl = cmds.rename(dup_ctrl, new_name)

    
    if mirror_axis == "X":
        cmds.setAttr(f"{dup_grp}.scaleX", -1)
    elif mirror_axis == "Y":
        cmds.setAttr(f"{dup_grp}.scaleY", -1)
    elif mirror_axis == "Z":
        cmds.setAttr(f"{dup_grp}.scaleZ", -1)

    
    cmds.makeIdentity(dup_grp, apply=True, t=True, r=True, s=True)

    return dup_grp, dup_ctrl

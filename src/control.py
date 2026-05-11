import maya.cmds as cmds


def apply_color(control):


    if control.startswith("L_"):
        color = 6   
    elif control.startswith("R_"):
        color = 13  
    else:
        return 

    shapes = cmds.listRelatives(control, shapes=True, fullPath=True)
    if shapes:
        for shape in shapes:
            cmds.setAttr(f"{shape}.overrideEnabled", 1)
            cmds.setAttr(f"{shape}.overrideColor", color)




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

    apply_color(ctrl)

    return grp, ctrl



def mirror_control(control):


    grp = cmds.listRelatives(control, parent=True, type="transform")[0]


    pos = cmds.xform(grp, q=True, ws=True, t=True)
    x, y, z = pos

    axis_values = {"X": abs(x), "Y": abs(y), "Z": abs(z)}
    mirror_axis = max(axis_values, key=axis_values.get)

    dup_grp = cmds.duplicate(grp, rr=True)[0]


    children = cmds.listRelatives(dup_grp, children=True, fullPath=True)
    dup_ctrl = [c for c in children if cmds.objectType(c) == "transform"][0]


    def swap_prefix(name):
        if name.startswith("L_"):
            return name.replace("L_", "R_", 1)
        if name.startswith("R_"):
            return name.replace("R_", "L_", 1)
        return name


    dup_grp = cmds.rename(dup_grp, swap_prefix(dup_grp))


    dup_ctrl = cmds.rename(dup_ctrl, swap_prefix(dup_ctrl))


    shapes = cmds.listRelatives(dup_ctrl, shapes=True, fullPath=True)
    if shapes:
        for shape in shapes:
            short = shape.split("|")[-1]
            cmds.rename(shape, swap_prefix(short))


    attrs = cmds.listAttr(dup_ctrl, userDefined=True) or []
    for attr in attrs:
        new_attr = swap_prefix(attr)
        if new_attr != attr:
            cmds.renameAttr(f"{dup_ctrl}.{attr}", new_attr)


    if mirror_axis == "X":
        cmds.setAttr(f"{dup_grp}.scaleX", -1)
    elif mirror_axis == "Y":
        cmds.setAttr(f"{dup_grp}.scaleY", -1)
    elif mirror_axis == "Z":
        cmds.setAttr(f"{dup_grp}.scaleZ", -1)


    cmds.makeIdentity(dup_grp, apply=True, t=True, r=True, s=True)


    apply_color(dup_ctrl)

    return dup_grp, dup_ctrl

import maya.cmds as cmds


def apply_color(control):
    """Applies color override based on prefix."""
    if control.startswith("L_"):
        color = 6   # Blue
    elif control.startswith("R_"):
        color = 13  # Red
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
    """Mirrors a control across the axis farthest from origin."""

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

    new_grp_name = swap_prefix(dup_grp)
    try:
        dup_grp = cmds.rename(dup_grp, new_grp_name)
    except RuntimeError:
        dup_grp = cmds.rename(dup_grp, new_grp_name + "_mirrored")

    new_ctrl_name = swap_prefix(dup_ctrl)
    try:
        dup_ctrl = cmds.rename(dup_ctrl, new_ctrl_name)
    except RuntimeError:
        dup_ctrl = cmds.rename(dup_ctrl, new_ctrl_name + "_mirrored")


    shapes = cmds.listRelatives(dup_ctrl, shapes=True, fullPath=True)

    if shapes:
        for shape in shapes:
            shape_full = cmds.ls(shape, long=True)[0]
            short = shape_full.split("|")[-1]
            new_name = swap_prefix(short)

            if new_name != short and new_name not in ("", None):
                try:
                    cmds.rename(shape_full, new_name)
                except RuntimeError:
                    pass


    if mirror_axis == "X":
        cmds.setAttr(f"{dup_grp}.scaleX", -1)
    elif mirror_axis == "Y":
        cmds.setAttr(f"{dup_grp}.scaleY", -1)
    elif mirror_axis == "Z":
        cmds.setAttr(f"{dup_grp}.scaleZ", -1)

    cmds.makeIdentity(dup_grp, apply=True, t=True, r=True, s=True)

    apply_color(dup_ctrl)

    return dup_grp, dup_ctrl

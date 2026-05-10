import maya.cmds as cmds


def create_cube_control(prefix="L", name="hand_ctrl", size=1.0, position=(0, 0, 0)):


    if prefix not in ["L", "R"]:
        prefix = "L"

    ctrl_name = f"{prefix}_{name}"
    grp_name = f"{ctrl_name}_grp"

    h = size * 0.5

    points = [
        (-h, -h, -h), (h, -h, -h),
        (h, -h, -h), (h, -h, h),
        (h, -h, h), (-h, -h, h),
        (-h, -h, h), (-h, -h, -h),

        (-h, -h, -h), (-h, h, -h),
        (h, h, -h), (h, -h, -h),

        (h, -h, h), (h, h, h),
        (h, h, -h), (h, h, h),
        (-h, h, h), (-h, -h, h),
        (-h, h, h), (-h, h, -h)
    ]

    ctrl = cmds.curve(name=ctrl_name, degree=1, point=points)
    grp = cmds.group(ctrl, name=grp_name)

    cmds.xform(grp, ws=True, t=position)
    cmds.makeIdentity(ctrl, apply=True, t=True, r=True, s=True)

    return grp, ctrl


def mirror_control(control, axis="X"):

    if control.startswith("L_"):
        new_prefix = "R_"
    elif control.startswith("R_"):
        new_prefix = "L_"
    else:
        raise ValueError("Control must start with L_ or R_")

    grp = cmds.listRelatives(control, parent=True)[0]

    dup_grp = cmds.duplicate(grp, name=grp.replace("L_", "R_").replace("R_", "L_"))[0]

    dup_ctrl = cmds.listRelatives(dup_grp, children=True)[0]
    new_ctrl_name = dup_ctrl.replace("L_", "R_").replace("R_", "L_")
    dup_ctrl = cmds.rename(dup_ctrl, new_ctrl_name)

    if axis.upper() == "X":
        cmds.setAttr(f"{dup_grp}.scaleX", -1)
    elif axis.upper() == "Y":
        cmds.setAttr(f"{dup_grp}.scaleY", -1)
    elif axis.upper() == "Z":
        cmds.setAttr(f"{dup_grp}.scaleZ", -1)

    cmds.makeIdentity(dup_grp, apply=True, t=True, r=True, s=True)

    return dup_grp, dup_ctrl

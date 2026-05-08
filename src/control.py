import maya.cmds as cmds


def create_cube_control(prefix="L_", name="hand_ctrl", size=1.0):

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

    cmds.xform(grp, worldSpace=True, pivots=(0, 0, 0))
    cmds.xform(ctrl, worldSpace=True, pivots=(0, 0, 0))

    cmds.makeIdentity(ctrl, apply=True, translate=True, rotate=True, scale=True)

    return grp, ctrl

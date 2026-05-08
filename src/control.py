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

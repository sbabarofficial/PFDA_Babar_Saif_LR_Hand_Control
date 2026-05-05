import maya.cmds as cmds


def create_cube_control(name="cube_ctrl", size=1.0):
    """
    Creates a resizable cube-shaped NURBS control curve at the origin,
    and places it inside a clean parent group.

    Args:
        name (str): Name of the control curve.
        size (float): Overall scale of the cube.

    Returns:
        tuple: (group, control)
    """

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

    
    ctrl = cmds.curve(name=name, degree=1, point=points)

    
    grp = cmds.group(ctrl, name=f"{name}_grp")

    
    cmds.xform(grp, worldSpace=True, pivots=(0, 0, 0))
    cmds.xform(ctrl, worldSpace=True, pivots=(0, 0, 0))

    
    cmds.makeIdentity(ctrl, apply=True, translate=True, rotate=True, scale=True)

    return grp, ctrl

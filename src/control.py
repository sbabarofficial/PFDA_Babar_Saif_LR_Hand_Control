import maya.cmds as cmds


def create_cube_control(name="cube_ctrl", size=1.0):
    """
    Creates a resizable cube-shaped NURBS control curve at the origin.
    The cube is made entirely of degree-1 curve segments (no surfaces).

    Args:
        name (str): Name of the control curve.
        size (float): Overall scale of the cube.

    Returns:
        str: The name of the created control curve.
    """

   


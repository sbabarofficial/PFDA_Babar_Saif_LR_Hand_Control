import maya.cmds as cmds


def main():
    """
    Main entry point for generating hand joints.

    Do not modify this function.
    """
    print("Creating hand joints...")
    joints = create_index_finger("L")
    print("Hand joints created:", joints)
    print("All done.")


def create_index_finger(side):
    """
    Creates a simple 3‑joint chain for the index finger.

    Args:
        side (str): "L" or "R" for left or right hand.

    Returns:
        list: A list of the created joint names.
    """
    cmds.select(clear=True)

    j1 = cmds.joint(name=f"{side}_index_01_jnt", position=(0, 0, 0))
    j2 = cmds.joint(name=f"{side}_index_02_jnt", position=(0, -1, 0))
    j3 = cmds.joint(name=f"{side}_index_03_jnt", position=(0, -2, 0))

    return [j1, j2, j3]


def create_finger(side, finger_name, positions):
    """
    Creates a finger joint chain with custom positions.

    Args:
        side (str): "L" or "R".
        finger_name (str): Name of the finger (e.g., "thumb", "middle").
        positions (list): List of (x, y, z) tuples for each joint.

    Returns:
        list: Joint names created for the finger.
    """
    cmds.select(clear=True)
    joints = []

    for i, pos in enumerate(positions, start=1):
        name = f"{side}_{finger_name}_{i:02d}_jnt"
        j = cmds.joint(name=name, position=pos)
        joints.append(j)

    return joints


if __name__ == "__main__":
    main()

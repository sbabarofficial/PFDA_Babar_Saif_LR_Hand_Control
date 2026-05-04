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




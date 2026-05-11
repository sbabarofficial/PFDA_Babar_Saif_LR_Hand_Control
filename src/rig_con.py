import maya.cmds as cmds
import control
import attributes

def get_user_position():
    sel = cmds.ls(selection=True)
    if not sel:
        print("No object selected. Control will be created at origin.")
        return (0, 0, 0)
    return cmds.xform(sel[0], q=True, ws=True, t=True)

def create_user_control():
    prefix = input("Enter prefix (L or R): ").strip().upper()
    size = float(input("Enter control size (e.g., 3): "))

    pos = get_user_position()
    name = f"{prefix}_hand_ctrl"

    grp, ctrl = control.create_cube_control(
        name=name,
        size=size,
        position=pos
    )

    attributes.add_hand_attributes(ctrl)

    print(f"Created control: {ctrl} at {pos}")
    return grp, ctrl

def mirror_user_control(ctrl):
    mirrored_grp, mirrored_ctrl = control.mirror_control(ctrl)
    attributes.add_hand_attributes(mirrored_ctrl)
    print(f"Mirrored control created: {mirrored_ctrl}")
    return mirrored_grp, mirrored_ctrl

def main():
    print("=== Maya Control Generator ===")
    print("Select an object in Maya to place the control at its position.")

    grp, ctrl = create_user_control()

    choice = input("Mirror this control to the opposite side? (y/n): ").strip().lower()
    if choice == "y":
        mirror_user_control(ctrl)

    print("Done!")

if __name__ == "__main__":
    main()

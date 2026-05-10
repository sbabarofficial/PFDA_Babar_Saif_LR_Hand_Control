import maya.cmds as cmds


def add_hand_attributes(control):


    fingers = ["fist", "fore", "mid", "ring", "pinky", "thumb"]
    created = []

    # Separator
    if not cmds.attributeQuery("Fingers", node=control, exists=True):
        cmds.addAttr(control, longName="Fingers", attributeType="enum", enumName="-----:")
        cmds.setAttr(f"{control}.Fingers", lock=True)
        created.append(f"{control}.Fingers")

    # Clench
    for finger in fingers:
        attr = f"{finger}_clench"
        min_val, max_val = (-10, 10) if finger == "fist" else (-5, 10)

        if not cmds.attributeQuery(attr, node=control, exists=True):
            cmds.addAttr(
                control,
                longName=attr,
                attributeType="float",
                minValue=min_val,
                maxValue=max_val,
                defaultValue=0,
                keyable=True
            )
            created.append(f"{control}.{attr}")

    # Twist
    for finger in fingers:
        attr = f"{finger}_twist"

        if not cmds.attributeQuery(attr, node=control, exists=True):
            cmds.addAttr(
                control,
                longName=attr,
                attributeType="float",
                minValue=-3,
                maxValue=3,
                defaultValue=0,
                keyable=True
            )
            created.append(f"{control}.{attr}")

    # Spread
    for finger in fingers:
        attr = f"{finger}_spread"

        if not cmds.attributeQuery(attr, node=control, exists=True):
            cmds.addAttr(
                control,
                longName=attr,
                attributeType="float",
                minValue=-5,
                maxValue=5,
                defaultValue=0,
                keyable=True
            )
            created.append(f"{control}.{attr}")

    return created

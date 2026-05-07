import maya.cmds as cmds


def add_hand_attributes(control):
   

    fingers = ["fist", "fore", "mid", "ring", "pinky", "thumb"]
    created = []


    if not cmds.attributeQuery("Fingers", node=control, exists=True):
        cmds.addAttr(control, longName="Fingers", attributeType="enum", enumName="-----")
        cmds.setAttr(f"{control}.Fingers", lock=True)
        created.append(f"{control}.Fingers")

   
    for finger in fingers:
        attr = f"{finger}_clench"

        if finger == "fist":
            min_val, max_val = -10, 10
        else:
            min_val, max_val = -5, 10

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

   
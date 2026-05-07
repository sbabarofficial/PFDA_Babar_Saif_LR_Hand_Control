import maya.cmds as cmds


def add_hand_attributes(control):
   
    fingers = ["fist", "fore", "mid", "ring", "pinky", "thumb"]
    categories = ["clench", "twist", "spread"]

    created = []

   
    if not cmds.attributeQuery("Fingers", node=control, exists=True):
        cmds.addAttr(control, longName="Fingers", attributeType="enum", enumName="-----")
        cmds.setAttr(f"{control}.Fingers", lock=True)
        created.append(f"{control}.Fingers")

   
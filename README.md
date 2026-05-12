# PFDA_Babar_Saif_proposal
# LR Hand Control Generator for Maya

## Demo
Video: https://youtu.be/8LaiRLt5ETw

## GitHub Repository
Repo: https://github.com/sbabarofficial/PFDA_Babar_Saif_LR_Hand_Control

## Description
The LR Hand Control Generator is a Python-based automation tool designed for Autodesk Maya. Its purpose is to streamline the rigging workflow by automatically generating clean, color‑coded, properly grouped hand controls for both the left and right sides of a character rig.

This tool reduces repetitive manual work by:
- Creating a control at the selected object’s position
- Applying correct naming conventions (L_ / R_)
- Automatically mirroring controls across the body
- Assigning color coding for easy visual identification
- Ensuring clean grouping and transforms for rig integration

This project demonstrates practical Python scripting for digital arts and media, focusing on efficiency, reliability, and real‑world rigging utility.

---

## Features
- Automatic control creation
- Side prefixing (L_ / R_)
- Automatic mirroring
- Color coding (blue for left, red for right)
- Clean grouping and transforms
- Safe renaming system to avoid Maya errors

---

## How to Install and Use This Tool in Maya

### 1. Download the Repository
Download or clone the project:

- Click the green **Code** button on GitHub  
- Select **Download ZIP**  
- Extract the folder anywhere on your computer  

Your folder should contain:

PFDA_Babar_Saif_LR_Hand_Control/
├── src/
│   ├── controllers.py
│   ├── rig_con.py
│   ├── attributes.py
│   ├── project.py
├── README.md
├── requirements.txt


---

### 2. Add the `src` Folder to Maya’s Python Path
In Maya:

1. Open **Windows → General Editors → Script Editor**
2. Switch to the **Python** tab
3. Run this (update the path):

---
### How to use - 
The prograne will give 3 prompts asking- 

1.Prefix (L/R)
2.Control size
3.Wether the user would like to mirror the control (this creates a 2nd instance of the control with the opposite orefix at the start)

```python
import sys
sys.path.append(r"C:/PATH/TO/PFDA_Babar_Saif_LR_Hand_Control/src")


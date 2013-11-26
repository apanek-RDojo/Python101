import maya.cmds as cmds
import json

# creates empty list to hold locator info
locator_info = []

# creates list to hold locator data. Will change later to accept text input as basis of list.
locList = ['lctr_l_arm1', 'lctr_l_arm2', 'lctr_l_wrist', 'lctr_l_armEnd']

# populates empty list with locators, positions and names based on input list data
def createLocators(locData, destList):
    for loc in locData:
	    cmds.spaceLocator(n=(loc), a=True)
	    cmds.xform (t=(locData.index(loc), 0, 0))
	    destList.append([loc, cmds.xform (q=True, t=True)])


createLocators(locList, locator_info)

# print statements
print locator_info

for locs in locator_info:
	print locs[0]
	print locator_info.index(locs)

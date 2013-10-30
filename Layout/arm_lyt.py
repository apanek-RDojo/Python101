import maya.cmds as cmds

# creates list to hold locator data
locData = ['loc1', 'loc2', 'loc3', 'loc4']

# populates list with locators, positions and names based on list data
for loc in locData:
	cmds.spaceLocator(n=(loc), p=(locData.index(loc), 0, 0))
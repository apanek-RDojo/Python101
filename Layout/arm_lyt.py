import maya.cmds as cmds
import json
import tempfile

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

# An empty dictionary that will be used to store locator_info
locator_info_dictionary = {}

# Assign locator_info to dictionary keys
       
locator_info_dictionary['names']= [locator_info[x][0] for x in range(len(locator_info))]
locator_info_dictionary['positions']= [locator_info[x][1] for x in range(len(locator_info))]

print locator_info_dictionary
data = locator_info_dictionary

# These functions can be used to read and write json
# Define a path to the json file.  Change this to a path on your computer.
fileName = 'D:/Users/Alice/Documents/GitHub/Python101/data/locator_info.json'

def writeJson(fileName, data):
	with open(fileName, 'w') as outfile:
		json.dump(data, outfile)

	file.close(outfile)

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
    
# Now we will save to a json file
writeJson(fileName, data)

# Read the Json file
data = readJson(fileName)
info = json.loads( data )
info2 = json.dumps( data )

# Now take a look at the different data types returned by loads and dumps
print type(json.dumps( data ))
print type(json.loads( data ))

for key, value in info.iteritems():
    print key, value

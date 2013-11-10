import sys
import os
import maya.cmds as cmds
print sys.path
 
sys.path.append('D:/Users/Alice/Documents/GitHub/Python101/')
cmds.evalDeferred('import system.startup')
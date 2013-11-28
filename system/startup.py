# Script from lecture
print 'Hello'
import maya.cmds as cmds
 
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )
 
def createMenu(*args):
    mi = cmds.window('MayaWindow', ma=True, q=True)
    for m in mi:
        if m == 'RDojo_Menu':
            cmds.deleteUI('RDojo_Menu', m=True)
 
    cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
    cmds.menuItem(label='Test 1')
    cmds.menuItem(label='Test 2')
 
createMenu()
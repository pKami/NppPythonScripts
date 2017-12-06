# File name: 		phpGenerateGettersSetters.py
# Author: 			Piotr Kaminski
# E-Mail: 			piotrkamx@gmail.com
# Date created:		April 2017
# Python Version:	2.6
# Description:
#	Simple plugin to generate getters and setters for PHP class members. Select the members and run the script.

import re

class GSTexts:
	getterText = """public function get%Propname%() {
	return $this->%propname%;
}
"""
	setterText = """public function set%Propname%($%propname%) {
	$this->%propname% = $%propname%;
}
"""

	@staticmethod
	def getGetterText(propname):
		return GSTexts.getterText.replace("%propname%", propname).replace("%Propname%", propname.title())
	
	@staticmethod
	def getSetterText(propname):
		return GSTexts.setterText.replace("%propname%", propname).replace("%Propname%", propname.title())
	
matches = []
def match_found(m):
    # append the match (start, end) positions to the matches array
    matches.append(m.group(2))

startPos = editor.getSelectionStart()
endPos = editor.getSelectionEnd()

if (endPos > startPos):
	propRegex = '^\s*(var|public|protected|private)\s+\$([\w\d_]+)'
	editor.research(propRegex, match_found, re.IGNORECASE, startPos, endPos)
	
	if (len(matches) > 0):
		editor.gotoPos(endPos)
		editor.addText('\n')
		for propname in matches:
			getterSetterText = '\n' + GSTexts.getGetterText(propname) + GSTexts.getSetterText(propname)
			editor.addText(getterSetterText)
	else:
		console.writeError('\nNo properties found in selection!')
else:
	console.writeError('\nNothing selected!')

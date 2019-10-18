# File name: 		invertCasing.py
# Author: 			Piotr Kaminski
# E-Mail: 			piotrkamx@gmail.com
# Date created:		October 2019
# Python Version:	2.6
# Description:
#	Simple script to invert LeTTer CasINg => lEttER cASinG

def replaceLine(contents, lineNumber, totalLines):
		editor.replaceLine(lineNumber, contents.strip().swapcase())
		return 1

editor.forEachLine(replaceLine)

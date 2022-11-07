# coding:			utf-8
# File name: 		naprawOgonki.py
# Author: 			Piotr Kaminski
# E-Mail: 			piotrkamx at gmail dot com
# Date created:		December 2019
# Python Version:	2.6
# Description:
#	Simple script to fix polish special characters after they've been improperly converted from ANSI/ASCII text file to UTF-8 text file

charsDict = {
  '¹' : 'ą', 
  '�' : 'Ą',
  'æ' : 'ć', 
  'Æ' : 'Ć', 
  'ê' : 'ę', 
  'Ê' : 'Ę',
  '³' : 'ł', 
  '£' : 'Ł', 
  'ñ' : 'ń',
  'Ñ' : 'Ń', 
#  'ó' : 'ó', 
#  'Ó' : 'Ó',
  'œ' : 'ś', 
  'Œ' : 'Ś', 
  'Ÿ' : 'ź', 
  '¥' : 'Ź', 
  '¿' : 'ż', 
  '¯' : 'Ż', 
}

def fixChars(str):
	for c in charsDict:
		str = str.replace(c, charsDict[c])
	return str

def replaceLine(contents, lineNumber, totalLines):
		newLineContents = fixChars(contents)
		if contents != newLineContents:
			editor.replaceLine(lineNumber, newLineContents.strip())
		return 1

editor.forEachLine(replaceLine)

# coding:			utf-8
# File name: 		naprawOgonki.py
# Author: 			Piotr Kaminski
# E-Mail: 			piotrkamx at gmail dot com
# Date created:		December 2019
# Python Version:	2.6
# Description:
#	Simple script to fix polish special characters after they've been improperly converted from ANSI/ASCII text file to UTF-8 text file

charsDict = {
  'Ê' : 'Ę',
#  'Ó' : 'Ó',
  '�' : 'Ą',
  'Œ' : 'Ś', 
  '£' : 'Ł', 
  '¯' : 'Ż', 
  '¥' : 'Ź', 
  'Æ' : 'Ć', 
  'Ñ' : 'Ń', 
  'ê' : 'ę', 
#  'ó' : 'ó', 
  '¹' : 'ą', 
  'œ' : 'ś', 
  '³' : 'ł', 
  '¿' : 'ż', 
  'Ÿ' : 'ź', 
  'æ' : 'ć', 
  'ñ' : 'ń',
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

uniqueLines = set()
linesToDelete = []
trim = True
removeEmpty = True

# --------------------------------------------------------
def appendLocalPath(lineContents, lineNumber, totalLines):	# function signature from documentation - must match forEachLine requirements
	if (trim):
		lineContents = lineContents.strip()
		editor.replaceLine(lineNumber, lineContents)
		
	if (removeEmpty and not lineContents):		# an empty string is just a falsy string
		linesToDelete.append(lineNumber)
		return

	if (lineContents in uniqueLines):
		linesToDelete.append(lineNumber)
	else:
		uniqueLines.add(lineContents)
# --------------------------------------------------------

editor.forEachLine(appendLocalPath)
for lineNo in linesToDelete[::-1]:
	editor.deleteLine(lineNo)
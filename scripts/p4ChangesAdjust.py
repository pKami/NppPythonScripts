# Adjust p4 changes format to a more conceise one.

# For reversing order, requires empty newline at the start of document,
# otherwise this latest change will be lost. This is added automatically.

# optionally reverse order
reverse = True
changes = []

def changelistReplace(m):
	return 'Submitted as p4 changelist #' + m.group(1) +':\r\n'

def changeFound(m):
	changes.append(m.group(1))

def reverseEntries():
	editor.documentStart()
	editor.newLine()	# insert a newline, required for the first regex match
	changeRegex = r"^$([\w\W]+?)^$";
	editor.research(changeRegex, changeFound)
	editor.clearAll()
	for ch in reversed(changes):
		editor.appendText(ch)
	editor.documentEnd()

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

editor.rereplace(r"Change (\d+) on .*$\s+", changelistReplace)
editor.replace('	- ', "- ")

if reverse:
	reverseEntries()

# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()
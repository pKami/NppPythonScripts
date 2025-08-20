# NppPythonScript: Open unique existing file paths listed in the current document

from Npp import notepad, editor
import os

def openFilesFromPathsInCurrentDoc():
    # Get all text from current document
    text = editor.getText()
    if not text.strip():
        notepad.messageBox("Document is empty.", "Info")
        return

    # Split into lines and strip whitespace
    # {curly braces} creates a set in Python. A set stores unique values only, as opposed to [list]
    unique_lines = {line.strip() for line in text.splitlines() if line.strip()}

    opened_count = 0
    skipped_count = 0
    skipped_paths = []   # collect paths that failed to open

    for line in unique_lines:
        if os.path.isabs(line) or os.path.exists(line):
            if os.path.isfile(line):
                try:
                    notepad.open(line)
                    opened_count += 1
                except Exception as e:
                    skipped_count += 1
                    skipped_paths.append("{} ({})".format(line, e))
            else:
                skipped_count += 1
                skipped_paths.append(line)
        else:
            skipped_count += 1

    # final summary message
    message = "Opened {} file(s).\nSkipped {} line(s).".format(opened_count, skipped_count)
    if skipped_paths:
        message += "\n\nFailed to open the following paths:\n"
        message += "\n".join(skipped_paths)

    notepad.messageBox(message, "openFilesFromPaths")

# Run
openFilesFromPathsInCurrentDoc()

# coding:			utf-8
# File name: 		naprawOgonki.py
# Author: 			Piotr Kaminski
# E-Mail: 			piotrkamx at gmail dot com
# Date created:		November 2018
# Python Version:	2.6
# Description:
#	This script replaces all diacritic characters (with "tails" or "dots"), where possible, with their closest non-diacritic equivalent

import unicodedata

# inspired by https://stackoverflow.com/a/517974
def normalize_str(input_ustr):
	encoding = "utf-8"
	unicode_string = input_ustr.decode(encoding)
	nfkd_form = unicodedata.normalize('NFKD', unicode_string)
	return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# inspired by https://stackoverflow.com/a/8935169/2588964
def asciify_latin_char(c):
	try:
		cname = unicodedata.name(c)
		if not cname.startswith('LATIN'):
			return c;
		
		cname = cname[:cname.index(' WITH')]
		return unicodedata.lookup(cname)
	except (ValueError, KeyError):
		return c

# this function has to match signature specified in the doc:
# http://npppythonscript.sourceforge.net/docs/latest/scintilla.html?highlight=foreach#Editor.forEachLine
def replaceDiacritics(contents, lineNumber, totalLines):
	normalized = normalize_str(contents.rstrip('\r\n'));
	withoutAccents = ''.join(asciify_latin_char(c) for c in normalized);
	editor.replaceLine(lineNumber, withoutAccents)


# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()	

editor.forEachLine(replaceDiacritics)

# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()
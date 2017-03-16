#!/usr/bin/env python
"""
Opens an IcoMoon SVG and generates the required CSS file.
"""

import os
import sys
from parsexml import *

defs = ParseXML(sys.argv[1]).data['svg']['defs']

for glyph in defs['font']['glyph']:
    if '_glyph-name' in glyph and '_unicode' in glyph:
        A = glyph['_unicode'] #.decode('utf-8')
        content = A.encode('ascii', 'backslashreplace')
        print """
.icon-%s:before {
  content: "%s";
}""" % (glyph['_glyph-name'], content.replace('\\\\u', '\\'))


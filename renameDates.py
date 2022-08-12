#! /usr/bin/env python3

# renameDates.py - Rename filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import os
import re
import shutil

datePattern = re.compile(r'''
    ^(.*?)
    ((0|1)?\d)-
    ((1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

# Loop over files in the working directory.

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# Skip files without a date.

    if mo == None:
        continue

# Get different parts of the filename.

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# Form the European filename.

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# TODO: Get the full, absolute file paths.

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# TODO: Rename the files.

    print('Renaming "%" to "%"...' (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)

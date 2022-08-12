#! /usr/bin/env python3
# countdown.py - A simple countdown script

import time
import subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['open', '/Users/dan/Downloads/Episode_1_Feb_11th_2006.mp3'])

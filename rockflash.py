#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import shutil

THRESHOLD = 200
file_list = []

try:
    root_dir = str (input('Directory with ROCK: '))
except ValueError:
    print("Nope :p")

if os.path.exists(root_dir) == False:
    print ('Wrong directory')
    input()
    exit()

try:
    output_dir = str (input('Output directory: '))
except ValueError:
    print("Nope :p")

if os.path.exists(output_dir) == False:
    print ('Wrong directory')
    input()
    exit()

try:
    THRESHOLD = int (input('Enter your THRESHOLD: '))
except ValueError:
    print("THRESHOLD = 200")

for top, dirs, nondirs in os.walk(root_dir):
    for name in nondirs:
        path = os.path.join(top, name)
        if path.lower().endswith('.mp3'): # endswith(('.mp3', '.flac'))
            file_list.append(path)

rc = len(file_list)
print ('Rock counter: ' + str(rc))
if THRESHOLD > rc:
    THRESHOLD = rc

files_to_write = random.sample(set(file_list), THRESHOLD)

print ("Let's Rock.")
for file in files_to_write:
    print (file)
    shutil.copy(file, output_dir)

input()
exit()

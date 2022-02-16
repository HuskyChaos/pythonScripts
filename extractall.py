#!/bin/python

import os
from zipfile import ZipFile

files = os.listdir(path='./')

for i in files:
    with ZipFile(i) as zf:
        zf.extractall()
    os.remove(i)

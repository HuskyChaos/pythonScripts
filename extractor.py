import os
from zipfile import ZipFile

firstName = 'flag'
lastName = '.zip'
fileNum = 100
firstPass = 'passwd'

while (fileNum>0):
    fullName = firstName + str(fileNum) + lastName
    finalPass = firstPass + str(fileNum)

    with ZipFile(fullName) as zf:
        zf.extractall(pwd=bytes(finalPass,'utf-8'))
    os.remove(fullName)
    fileNum-=1
#                   IMPORTS
import os
import sys

#                   FUNCTIONS
def getDirName(dirPath):
    return dirPath.split('\\')[len(dirPath.split('\\')) - 1]

# make sure that they have the correct number of arguments
if(len(sys.argv) != 2):
    print("Please input the correct number of arguments")
    exit()

if not os.path.isdir(sys.argv[1]):
    print("Please input a correct path to a directory")
    exit()

count = 0
first = 0
rootDir = sys.argv[1]
startSlash = rootDir.count('\\')

for dirName,subdirList, fileList,in os.walk(rootDir):

    count = dirName.count('\\') - startSlash - 1

    for x in range(0,count):
        print('   ', end = '')
    if first == 0:
        first = 1
        print('[%s]' % dirName)
    else:
        print('|--[%s]' % getDirName(dirName))

    for fname  in fileList:
        for x in range(0,count+1):
            print('   ', end = '')
        print('|--{%s}' % fname)

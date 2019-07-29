# neisesmike
# 30 sept 2018
# python 2
# script to remove 'gibberish' files from a directory
# gibberish: 'not english' as per google's langdetect

import os
# remark: I wonder how slow this is...
# it detects only natural languages
from langdetect import detect

# get a listing of all files in the directory
fileList = os.listdir( os.getcwd() ) 

# create* new dir for target files
try:
    os.mkdir("englishFiles")
except:
    print( "The englishFiles directory already exists." )

# move english files to englishFiles
for fileName in fileList:
    if( fileName == 'englishFiles' or fileName == 'gibberishFilter.py' ):
        continue

    thisFile = open(fileName, 'r')
    thisString = thisFile.read();
    language = detect( thisString )

    if( language != 'en' ):
        continue

    oldName = thisFile.name
    newName = "englishFiles/"+oldName
    os.rename( oldName, newName ) 

    thisFile.close()

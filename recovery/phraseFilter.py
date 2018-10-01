# neisesmike
# 30 sept 2018
# python 2
# script to remove 'gibberish' files from a directory
# gibberish: 'not english' as per google's langdetect

import os
import time

def camelfy( phrase ):
    # convert phrase to camel case
    phraseDir = phrase.title()
    phraseDir = phraseDir[0].lower() + phraseDir[1:]
    phraseDir = phraseDir.replace(" ", "")
    return phraseDir 

start = time.time()

# get a listing of all files in the directory
fileList = os.listdir( os.getcwd() ) 

# take user input for search phrase
thisInput = raw_input("By what phrase shall I search?")

phrases = []
while( thisInput != 'x' ):
    phrases.append(thisInput)
    thisInput = raw_input("What other phrases?")

# move matching files to the new directory
for fileName in fileList:

    # don't search through directories or this file
    if( os.path.isdir( fileName ) or fileName == 'phraseFilter.py' ):
        continue

    thisFile = open(fileName, 'r')
    thisString = thisFile.read();

    for phrase in phrases:
        if phrase in thisString:
            phraseDir = camelfy(phrase)
            try:
                os.mkdir(phraseDir)
            except:
                pass
            oldName = thisFile.name
            newName = phraseDir + "/" + oldName
            os.rename( oldName, newName ) 
            thisFile.close()
            break

    thisFile.close()

end = time.time()
print("That took me " + str(end-start) + " seconds.")

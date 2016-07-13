#! /usr/bin/python

#Compares the suffixes of one seq to the prefixes of all other sequences
def function(rosID, string):
    k = 3
    counter = 0
    suffix = string[len(string) - k:]
    #print 'suffix = ' + suffix
    #print 'id = ' + rosID
    for key in seqDict:
        prefix = seqDict[key][:k]
        #print 'prefix ' + prefix
        if suffix == prefix and key != rosID:
            print rosID + ' ' + key
    return None


# Read in FASTA file, make a dict
inFile = open('ex_GRPH_test.txt', 'r')
count = -1
seqDict = {}
for line in inFile:
    line = line.strip()
    if line[0] == '>':
        count += 1
        seqKey = line[1:]
        seqDict[seqKey] = ''
    else:
        if count > -1:
            seqDict[seqKey] += line

# Loops through rosID's
for rosID in seqDict:
    function(rosID, seqDict[rosID])

print "My name is Sam"

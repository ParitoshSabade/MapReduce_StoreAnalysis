#!/usr/bin/python

import sys

# Code for: Sales per Category 

salesTotal = 0.0
oldKey = None


#for line in sys.stdin:
#    data_mapped = line.strip().split("\t")
#    if len(data_mapped) != 2:
#        # Something has gone wrong. Skip this line.
#        continue
#
#    thisKey, thisSale = data_mapped
#    
#    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", salesTotal
#        salesTotal = 0
#
#    oldKey = thisKey
#    salesTotal += float(thisSale)
#
#if oldKey != None:
#    print oldKey, "\t", salesTotal
    

##############################################################################


# Code for: Highest Sale 


#for line in sys.stdin:
#    data_mapped = line.strip().split("\t")
#    if len(data_mapped) != 2:
#        # Something has gone wrong. Skip this line.
#        continue
#
#    thisKey, thisSale = data_mapped
#    
#    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", salesMax
#        salesMax = 0.0
#
#    oldKey = thisKey
#    if float(thisSale) > salesMax:
#      salesMax = float(thisSale)
#
#if oldKey != None:
#    print oldKey, "\t", salesMax



##############################################################################


    
# Code for: Total Sale 


SalesTotal = 0.0
count = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    
    oldKey = thisKey
    count += 1
    salesTotal += float(thisSale)

if oldKey != None:
    print "{0}\t{1}".format(count, salesTotal)
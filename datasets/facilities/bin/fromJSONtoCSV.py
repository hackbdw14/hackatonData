__author__ = 'Oscar'

import rdflib
import sys
import os
import pprint
import re
import csv
import json


for name in ['allotjament','centres_informacio','comercial','cultura','educacio','esports','mediambient','sanitat','serveis_socials','transports']:

    FILE_IN = "../data/" + name + ".json"

    FILE_OUT = "../data/" + name + ".csv"

    print "Converting %s to %s" % (FILE_IN,FILE_OUT)

    fileIn = open(FILE_IN,"rb")

    myJSON = json.load(fileIn)

    fileIn.close()

    myData = []
    myHeader = ['id','lat','lon','address','created','district','name','neighborhood','postalCode','cat']

    for feature in myJSON['features']:
        oneData = {}

        oneData['lat'] = feature['geometry']['coordinates'][1]
        oneData['lon'] = feature['geometry']['coordinates'][0]
        oneData['id'] = feature['id']
        for name in ['address','created','district','name','neighborhood','postalCode']:
            if name in feature['properties']:
                oneData[name] = feature['properties'][name].encode("utf8")
            else:
                oneData[name] = "None"

        for cat in feature['properties']['cats']:
            oneData['cat'] = cat.encode("utf8")
            myData.append(oneData)


    fileOut = open(FILE_OUT,"wb")

    csvWriter = csv.writer(fileOut)

    csvWriter.writerow(myHeader)

    for entry in myData:
        row = [entry[property] for property in myHeader]
        csvWriter.writerow(row)

    fileOut.close()


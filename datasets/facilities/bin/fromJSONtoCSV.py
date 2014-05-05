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



#
# def makeGeoJSON(myList):
#
#     myJSON = {}
#
#     myJSON['type'] = "FeatureCollection"
#     myJSON['features'] = []
#
#     for feature in myList:
#
#         pprint.pprint(feature)
#         myFeature = {}
#
#         myFeature['type'] = 'Feature'
#         myFeature['geometry'] = {"type": "Point", "coordinates" : [float(feature['lon']),float(feature['lat'])]}
#         myFeature['id'] = feature['id']
#         myFeature['properties'] = {'id': feature['id']}
#
#         for key in feature.keys():
#             if key not in ['id','lat','lon']:
#                 myFeature['properties'][key] = feature[key]
#
#         myJSON['features'].append(myFeature)
#
#     return myJSON
#
# # First read categories
#
# fileIn = open(FILE_IN,"rbU")
#
# inConcept = False
#
# catData = {}
# id = -1
#
#
# for line in fileIn:
#     line = line.rstrip().decode("utf8")
#     if re.search(r'<skos:Concept', line) is not None:
#         inConcept = True
#     else:
#         if re.search(r'</skos:Concept', line) is not None:
#             inConcept = False
#         if inConcept:
#             match = re.search(r'<dct:identifier>(.*)</dct:identifier>',line)
#             if match:
#                 id = "#c" + match.group(1)
#             match = re.search(r'<skos:prefLabel xml:lang="ca">(.*)</skos:prefLabel>',line)
#             if match:
#                 catData[id] = match.group(1)
#
# fileIn.close()
#
# #pprint.pprint(catData)
#
#
# # Second, read vcards
# fileIn = open(FILE_IN,"rbU")
#
# inVCard = False
#
# allData = []
#
# for line in fileIn:
#     line = line.rstrip().decode("utf8")
#     if re.search(r'<v:VCard', line) is not None:
#         inVCard = True
#         myData = {}
#     else:
#         if re.search(r'</v:VCard', line) is not None:
#             inVCard = False
#             allData.append(myData)
#         if inVCard:
#             match = re.search(r'<dct:identifier>(.*?)</dct:identifier>',line)
#             if match:
#                 myData['id'] = match.group(1)
#
#             match = re.search(r'<v:fn>(.*?)</v:fn>',line)
#             if match:
#                 myData['name'] = match.group(1)
#
#             match = re.search(r'<v:street-address>(.*?)</v:street-address>',line)
#             if match:
#                 myData['address'] = match.group(1)
#
#             match = re.search(r'<xv:district>(.*?)</xv:district>',line)
#             if match:
#                 myData['district'] = match.group(1)
#
#             match = re.search(r'<xv:neighborhood>(.*?)</xv:neighborhood>',line)
#             if match:
#                 myData['neighborhood'] = match.group(1)
#
#             match = re.search(r'<v:postal-code>(.*?)</v:postal-code>',line)
#             if match:
#                 myData['postalCode'] = match.group(1)
#
#             match = re.search(r'<v:latitude>(.*?)</v:latitude>',line)
#             if match:
#                 myData['lat'] = match.group(1)
#
#             match = re.search(r'<v:longitude>(.*?)</v:longitude>',line)
#             if match:
#                 myData['lon'] = match.group(1)
#
#             match = re.search(r'<v:category rdf:resource="http://www.bcn.cat/data/asia/categories#(.*?)"/>',line)
#
#             if match:
#                 cat = "#"+match.group(1)
#                 if 'cats' not in myData:
#                     myData['cats'] = []
#                 if cat in catData:
#                     if catData[cat] not in myData['cats']:
#                         myData['cats'].append(catData[cat])
#
#             match = re.search(r'<dct:created>(.*?)</dct:created>',line)
#
#             if match:
#                 myData['created'] = match.group(1) + "Z"
#
#
#
#
# fileIn.close()
#
# myStruct = makeGeoJSON(allData)
#
# #pprint.pprint(myStruct)
#
# # Wrote final geoJSON
#
# fileOut = open(FILE_OUT,"wb")
#
# json.dump(myStruct,fileOut)
#
# fileOut.close()

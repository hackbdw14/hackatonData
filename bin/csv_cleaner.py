# -*- coding: utf-8 -*-

import sys
import json
import re
import codecs


def clean_string(text):
    #print "ANTES2 --%s--" % text
    #print re.findall(re.compile(u'[^áéíóúàèìòùÁÉÍÓÚÀÈÌÒÙa-zA-Z0-9.,\s]'),text)
    #text = re.sub(re.compile(u'[^áéíóúàèìòùÁÉÍÓÚÀÈÌÒÙa-zA-Z0-9.,\s]'),'',text)
    text = re.sub('\xc2','',text)
    text = re.sub('\xa0','',text)
    #text = re.sub('\s+$','',text)
    #text = re.sub('^\s+','',text)
    text = re.sub('"','',text)

    #print "DESPUES2 --%s--" % text

    return text

for path in sys.argv[1:]:
    print path
    print path.split(".csv")[0]+"OK.csv"
    lines = list()
    with codecs.open(path,'r','utf-8') as csv2clean:
        for line in csv2clean:
            line_parts = line.split(",")
            cleaned_line_parts = list()
            for line_part in line_parts:
                #print "ANTES --%s--" % line_part.encode("utf-8")
                print "ANTES --%s--" % line_part
                print "DESPUES --%s--" % clean_string(line_part).strip()
                cleaned_line_parts.append(clean_string(line_part).strip())
            lines.append(",".join(cleaned_line_parts))

    with codecs.open(path.split(".csv")[0]+"OK.csv",'w','utf-8') as exit_file:
        for line in lines:
            exit_file.write(line+"\n")

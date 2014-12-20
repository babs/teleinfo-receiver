#!/usr/bin/python

import lzma, json, glob, sys
from pprint import pprint

def main():
    values = {}
    i = 0.
    for f in glob.glob("dumps/*"):
        content = json.load(open(f,'r'))
        values[content['tramets']]=content['trame']
        i+=1
    rawjson = json.dumps(values)
    compressedjson = lzma.compress(rawjson,options={'level':6,'extreme':True})
    print 'Elements:  %8d'%i
    print 'Raw size:  %8d'%len(rawjson)
    print 'LZMA size: %8d'%len(compressedjson)
    print 'Size/raw element:  %6.2f'%(len(rawjson)/i)
    print 'Size/comp element: %6.2f'%(len(compressedjson)/i)
    print '--'
    print "raw size/day:   %10d"%((len(rawjson)/i)*(86400/2))
    print "comp size/day:  %10d"%((len(compressedjson)/i)*(86400/2))
    print "raw size/year:  %10d M"%((len(rawjson)/i)*(86400/2)*365/1024**2)
    print "comp size/year: %10d M"%((len(compressedjson)/i)*(86400/2)*365/1024**2)
    open('out','w').write(rawjson)
    open('out.xz','w').write(compressedjson)

if __name__ == "__main__":
    main()

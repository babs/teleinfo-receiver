#!/usr/bin/python

import lzma, json, glob, sys
from pprint import pprint

def main():
    trames = filter(lambda x: x != "dumps/.placeholder", glob.glob("dumps/*"))
    trames.sort()

    cnt = {}
    currank = {}
    prevrank = None
    donerank = []

    for f in trames:
        t = json.load(open(f, 'r'))
        rank = int(t['tramets'] / 50000)
        rank *= 50000
        currank.update({t['tramets']:t['trame']})
        if prevrank != None and prevrank != rank and rank > prevrank:
            donerank.append(prevrank)
            print "Rank %d done, compressing..."%(rank)
            fp = lzma.LZMAFile('archives/%d.json.xz'%rank, 'w', options={'level':9, 'extreme': True})
            json.dump(currank, fp)
            fp.close()
        prevrank = rank
                
        
        if rank in cnt:
            cnt[rank] += 1
        else:
            cnt[rank] = 1
        #print rank
        #print "%.6f"%t['tramets']
    pprint(cnt)
    pprint(donerank)
    

if __name__ == "__main__":
    main()

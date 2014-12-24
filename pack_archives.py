#!/usr/bin/python

import lzma, json, glob, sys, os
from pprint import pprint
from Colorize import init_root_logger

log = init_root_logger()

def archive_rank(rank, currank, currankfiles):
    log.info( "Rank %d done, compressing..."%(rank))
    archivename = 'archives/%d.json.xz'%rank
    if os.path.exists(archivename):
        try:
            existingframes = json.load(lzma.LZMAFile(archivename, 'r'))
            currank.update(existingframes)
        except:
            # Skip loop avoid rewrite
            log.warning("Unable to load existing frames, not archiving.")
            return

    log.debug("compressing")
    compressedvalue = lzma.compress(json.dumps(currank), options={'level':9, 'extreme': True})
    log.debug("saving")
    fp = open(archivename, 'w')
    fp.write(compressedvalue)
    fp.close()
    log.debug("cleaning")
    for framefile in currankfiles:
        os.unlink(framefile)
        #sys.exit(0)
        #pass


def main():
    trames = filter(lambda x: x != "dumps/.placeholder", glob.glob("dumps/*"))
    trames.sort()

    cnt = {}
    currank = {}
    currankfiles = []
    prevrank = None
    donerank = []

    for f in trames:
        t = json.load(open(f, 'r'))
        rank = int(t['tramets'] / 50000)
        rank *= 50000

        # format float as string for json representation. %.6f
        # if not, releading existing frames make double entries when serialized
        currank["%.6f"%t['tramets']] = t['trame']
        currankfiles.append(f)
        if prevrank != None and prevrank != rank and rank > prevrank:
            archive_rank(rank, currank, currankfiles)
            donerank.append(prevrank)
            currank = {}
            currankfiles = []
        prevrank = rank
        
        if rank in cnt:
            cnt[rank] += 1
        else:
            cnt[rank] = 1
        #print rank
        #print "%.6f"%t['tramets']

    #for rank in cnt:
    #    log.info("Rank %d: %d items"%(rank, cnt[rank]) )
    if len(donerank) > 0:
        log.info("Archived ranks: %s."%(", ".join(map(lambda x: str(x), donerank))) )
    

if __name__ == "__main__":
    main()

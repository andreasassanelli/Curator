import os
import xxhash
import hashlib
from threading import Thread
import time
import logging

# FileScanner Threaded Class
#
# Each FS instance implements one scanning thread
#
# Attributes requiredd:
#  
#
#
class FileScanner(Thread):
    
    # Scanner parameters
    scannerBasePath = ""                        # Hold the root folder where the scanner will be looking at
    scannerCalcCRC32 = True                     # Should I calculate each file's crc-32?
    scannerCalcMD5 = True                       # Should I calculate each file's md5 checksum?
    scannerCalcSHA1 = True                      # Should I calculate each file's sha-1 checksum?
    scannerCalcxxHash = False                   # Should I calculate each file's xxHash checksum?

    def scanNow(self, scanPath):
        #Scan a directory
        print("Scanning %s" % scanPath)
        items = os.listdir(scanPath)
        for item in items:
            if os.path.isdir(scanPath + item):
                print("Directory found: %s" % scanPath + item)
                self.scanNow(scanPath + item + "\\")
            else:
                #print(os.stat(scanPath + item))
                # This is an actual file! Let's scan it!
                self.scanFile(scanPath + item)
                pass

    def scanFile(self,filepath):
        # Scan a single file
        print("Scanning file: %s" % filepath)
        BLOCKSIZE = 65536
        hasher_sha1 = hashlib.sha1()
        hasher_md5 = hashlib.md5()
        with open(filepath, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            buf2 = buf
            buf3 = buf
            while len(buf) > 0:
                hasher_sha1.update(buf)
                hasher_md5.update(buf2)
                buf = afile.read(BLOCKSIZE)
                buf2 = buf
                buf3 = buf
        this_md5 = hasher_md5.hexdigest()
        print("MD5: %s" % this_md5)
        this_sha1 = hasher_sha1.hexdigest()
        print("SHA-1: %s" % this_sha1)
        pass

    def __init__(self, scanPath, doCRC32=True, doMD5=True, doSHA1=True, doxxHash= False):
        Thread.__init__(self)
        self.scannerBasePath = scanPath
        self.scannerCalcCRC32 = doCRC32
        self.scannerCalcMD5 = doMD5                 
        self.scannerCalcSHA1 = doSHA1                  
        self.scannerCalcxxHash = doxxHash
    def run(self):
        print ("Thread '" + self.name + "' avviato")
        self.scanNow(self.scannerBasePath)
        print ("Thread '" + self.name + "' terminato")
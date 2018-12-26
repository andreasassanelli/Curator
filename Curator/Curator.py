import os, sys
import logging
import threading
from stat import *

#import modules
import ingestDATs
import FileScanner

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

def main(args):
    # Set-up logging facility
    logging.basicConfig(filename='C:\\curator\\curator.log', level=logging.DEBUG)
    logging.info('Session Started - ')
    logging.debug("Launch Arguments: ")

    # Start the program (artificial)
    xml_filepath = "C:\\curator\\dats\\dat.xml"
    xml_dat_file = ingestDATs.XmlDATFile(xml_filepath)

    scanThread = FileScanner.FileScanner('C:\\curator\\in\\')
    scanThread.start()
    scanThread.join()

    logging.info('Session Finished - ')

if __name__ == '__main__':
    #walktree(sys.argv[1], visitfile)
    #walktree(input(), visitfile)
    main(sys.argv[1:])
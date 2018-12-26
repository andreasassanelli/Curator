from xml.dom.minidom import parse
import xml.dom.minidom
import logging

class XmlDATFile:

    # Format of the DAT file in momory:
    # ---------------------------------
    # DATA STRUCTURE: Dictionary
    #
    # Each item is keyed by a set
    # {file_size, file_sha256, file_sha1, file_md5}
    # Each item contains a dictionary of information
    # {
    #   mandated_path                   'relative path to file for renaming
    #   mandated_file_name              'The filename used for renaming
    #   file_time                       'Set of file timestamps?
    #   datfile_description             'Name/Description of the originating DAT File
    #
    #
    #
    dat_filepath = None
    dat_contents = dict()

    def loadDATFile(self, filepath):
        # Open XML document using minidom parser
        DOMTree = xml.dom.minidom.parse(filepath)
        datfile = DOMTree.documentElement
        if datfile.hasAttribute("datfile"):
           print ("Root element : %s" % datfile.getAttribute("datfile"))

        # Get all the machines in the datfile (a "machine" is a set of ROMs)
        machines = datfile.getElementsByTagName("machine")

        #Set-up the work variables
        this_machine = dict()
        this_rom = dict()
        romset = list()

        # Traverse the datfile for each machine
        for machine in machines:
            print ("******machine******")
            logging.info("******machine******")

            if machine.hasAttribute("name"):
              print ("Title: %s" % machine.getAttribute("name"))
              logging.info("Title: %s" % machine.getAttribute("name"))
              
              this_machine['description'] = machine.getElementsByTagName('description')[0].childNodes[0].data
              print ("ROMSet: %s" % this_machine['description'])
              logging.info("ROMSet: %s" % this_machine['description'])

            roms = machine.getElementsByTagName("rom")
            # Traverse the single machine for every ROM
            romset.clear
            i = 0
            for rom in roms:
                print ("-----ROM-----")
                logging.info("-----ROM-----")

                this_rom['name'] = rom.getAttribute('name')
                print ("name: %s" % this_rom['name'])
                logging.info("name: %s" % this_rom['name'])
                this_rom['size'] = rom.getAttribute('size')
                print ("size: %s" % this_rom['size'])
                logging.info("size: %s" % this_rom['size'])
                this_rom['crc'] = rom.getAttribute('crc')
                print ("crc: %s" % this_rom['crc'])
                logging.info("crc: %s" % this_rom['crc'])
                this_rom['md5']  = rom.getAttribute('md5')
                print ("md5: %s" % this_rom['md5'])
                logging.info("md5: %s" % this_rom['md5'])
                this_rom['sha1']  = rom.getAttribute('sha1')
                print ("sha1: %s" % this_rom['sha1'])
                logging.info("sha1: %s" % this_rom['sha1'])
                # Add the current temporary list to single romset list
                romset.append(this_rom)
                i = i + 1

    # Constructor
    def __init__(self, filepath):
        dat_filepath = filepath
        self.loadDATFile(filepath)

#Ingest DAT Files
def ingestXMLDAT(xmldatfile):
    pass

def ingestCMPDAT(cmpdatfile):
    pass
#! python3
# Copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os
import argparse
import logging


def zipFolder(folder, outfile):
    # Backup the entire contents of "folder" into a zip file.

    #folder = os.path.abspath(folder) # make sure folder is absolute

    # Create the zip file.
    backupZip = zipfile.ZipFile(outfile, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        logging.info('Adding files in {}...'.format(foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            logging.debug("Adding {} file to zip".format(filename))
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    logging.info('{} created.'.format(backupZip.filename))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=str, help="Directorio a comprimir")
    parser.add_argument("-o", "--outfile", dest="outfile", type=argparse.FileType('wb'), help="Nombre de fichero zip de salida. Por defecto, out.zip", default=open("out.zip", "wb"))
    parser.add_argument("-v", "--verbose", dest="verbose_count", action="count", default=0, help="Incrementa la verbosidad por cada ocurrencia")

    args = parser.parse_args()
    
    """
    Those are the values for logging levels
    CRITICAL 	50
    ERROR 	    40
    WARNING 	30
    INFO 	    20
    DEBUG 	    10
    NOTSET 	    0
    """
    
    # Sets log level to WARN going more verbose for each new -v. 
    level = max(3 - args.verbose_count, 0) * 10
    logging.basicConfig(level=level)

    logging.info("Creating {}".format(args.outfile.name))
    zipFolder(args.folder, args.outfile)

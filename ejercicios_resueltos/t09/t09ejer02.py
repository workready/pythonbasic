import threading, zipfile, os

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
        
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of {}'.format(self.infile))


background = AsyncZip(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'stockholm_td_adj.tsv'), 'stockholm_td_adj.zip')

# Inicia el proceso asincrono y espera a que termine
background.start()
print('Se va a crear un fichero zip en un hilo aparte.')

background.join() # Wait for the background task to finish
print('Hilo terminado.')
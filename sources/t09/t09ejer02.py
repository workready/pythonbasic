import threading, zipfile, os

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
        
    def run(self):
        # Tu codigo aqui


background = AsyncZip(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'stockholm_td_adj.tsv'), 'stockholm_td_adj.zip')

# Inicia el proceso asincrono y espera a que termine
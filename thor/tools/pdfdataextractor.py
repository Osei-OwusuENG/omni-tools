import pdfplumber
import pandas as pd
import glob
import os


class extractor():
    def __init__(self):
        self.extracted = []
        pass
    
    def extract_tables(self, foldername):

        files = glob.glob(os.path.join('./data', foldername))

        for file in files:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    table = page.extract_tables()
                    if table:
                        self.extracted.append({
                            'source': file,
                            'page': page.page_number,
                            'table': table
                            })

        return self.extracted
    

    def extract_text(self, foldername):

        files = glob.glob(os.path.join('./data', foldername))

        for file in files:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    table = page.extract_text()
                    if table:
                        self.extracted.append({
                            'source': file,
                            'page': page.page_number,
                            'table': table
                            })

        return self.extracted






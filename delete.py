import os
from glob import glob
import pandas as pd


files = glob('./data/output/*.csv')
print(len(files))
print('I am working on it')
for file in files:
    parts = os.path.basename(file).replace('.csv', '').split('_')

    try:
        df = pd.read_csv(file, header=None)
    except pd.errors.EmptyDataError:
        print('pd.errors.EmptyDataerror')
        print(f'empty, removing empty file:', file)
        os.remove(file)
        continue
    except Exception as e:
        print(f'error reading {file}:', e)
        continue

    if df.empty:
        print(f'removing empty file:', file)
        os.remove(file)
        continue

    if parts[1].lower() in ['cover page 2', 'hidden', 'hidden regions', 'evidence pack',  'ee measures', 'sec tool version']:
        try:
            print(f'removing file:', file)
            os.remove(file)
        except Exception as e:
            print(f'error:', e)
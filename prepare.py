import pandas as pd
from glob import glob
import os

columns_2 = ['building_id','total_floor_area_m2', 'total_floor_volume_m3', 'avg_floor_height_m']
files = glob('./data/output/*.csv')

for file in files:

    parts = os.path.basename(file).split('_')

    if parts[1].lower() == 'general dimensions' and parts[2].lower() in ['table1', 'table5']:
        # read file using pandas
        df = pd.read_csv(file)

        # 
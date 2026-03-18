import pandas as pd
from glob import glob
import os

columns_2 = ['building_id','total_floor_area_m2', 'total_floor_volume_m3', 'net_floor_area_m2', 'net_floor_volume_m3', 'avg_floor_height_m']
files = glob("C:/Users/USER/output/*.csv")


building_geometry = {}

for file in files:

    parts = os.path.basename(file).split('_')

    if parts[1].lower() == 'general dimensions':
        try:
            # read file using pandas
            df = pd.read_csv(file, header=None, skiprows=2)
            print(df.head())

            # create a row for each building_id
            b_id = os.path.basename(file).replace('.csv', '').split('_')[0]

            if not b_id in building_geometry:
                building_geometry[b_id] = {col: None for col in columns_2}
                building_geometry[b_id]['building_id'] = b_id
            
            try:
                # for each building id extract total floor area
                floor_area = df.loc[df.iloc[:, 0].astype(str).str.contains('gf|net floor|real|net', case=False, na=False), 1].iloc[0]
                print(b_id, f'floor area',floor_area)
                building_geometry[b_id]['net_floor_area_m2'] = floor_area

                # for each building id extract total floor volume
                floor_volume = df.loc[df.iloc[:, 2].astype(str).str.contains('gf|net volume', case=False, na=False), 3].iloc[0]
                print(b_id, f'floor volumne', floor_volume)
                building_geometry[b_id]['net_floor_volume_m3'] = floor_volume
            except Exception as e:
                print(f'error in {file}: {e}')

            try:
                # calculate avg_floor_height
                total_height = pd.to_numeric(df.iloc[:, 4]).sum()
                num_floor = len(df.iloc[:, 5])
                building_geometry[b_id]['avg_floor_height_m'] = total_height/num_floor

                # extract total floor area and volume
                total_floor_area = pd.to_numeric(df.iloc[:, 3]).sum()
                building_geometry[b_id]['total_floor_area_m2'] = total_floor_area

                total_floor_volume = pd.to_numeric(df.iloc[:, 7]).sum()
                building_geometry[b_id]['total_floor_volume_m3'] = total_floor_volume
            except Exception as e:
                print(f'error in {file}: {e}')

        except Exception as e:
            print(f'error in {file}: {e}')


df = pd.DataFrame(building_geometry.values())

df.to_csv('./data/combined/cleaned_geometry_building_data.csv', index=False)

print(len(files))
print(len(df))

print(df.head())


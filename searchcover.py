import glob
import re
import os   
import pandas as pd


# files = glob.glob('./data/output/*.csv')
# file1 = []
# for file in files:

#     basename = os.path.basename(file).removesuffix('.csv')

#     match = re.search(r'^1_', basename)
#     if match:
#         file1.append(file)



# # print(len(file1))
# # print(file1[:60])

# # print(len(files))

columns_1 = ['building_id', 'longitude', 'latitude', 'town', 'construction_year', 'energy use (kWh/yr)', 'kg CO2/year', 'total_floor_area_m2', 'num_floors', 'occupied_area_m2', 'ac_area_m2', 'ac_coverage_ratio', 'has_ac', 'has_hot_water']
files = list(glob.glob('./data/output/*.csv'))
curated_files = [file for file in files if os.path.basename(file).replace('.csv', '').split('_')[1].lower() == 'cover page']
print(len(curated_files))
all_data = []

# df = pd.DataFrame(data=all_data, columns=columns_1)

# df.to_csv('./data/combined/clean_building_data.csv', index=False)

building_records = {}

for file in curated_files:

    try:

        # READ FILES
        df = pd.read_csv(file, header=None, skiprows=1)

        # SKIP EMPTY FILES
        if df.empty:
            continue
        
        # EXTRACT WANTED DATA
        parts = os.path.basename(file).replace('.csv', '').split('_')
        b_id = parts[0]

        if not b_id in building_records:
            building_records[b_id] = {col: None for col in columns_1}
            building_records[b_id]['building_id'] = b_id
        
        try:
            head_idx_mask = df.iloc[:, 0].str.contains('coordinates', case=False, na=False)

            if head_idx_mask.any():
                head_idx = df.index[head_idx_mask][0]
                print(head_idx)

                val_lng = df.iloc[head_idx + 1, 2]
                building_records[b_id]['longitude'] = val_lng

                val_lt = df.iloc[head_idx + 1, 1]
                building_records[b_id]['latitude'] = val_lt
        except:
            pass
        try:
            val_t = df.loc[df.iloc[:, 0].str.contains('town', case=False, na=False), 1].iloc[0]
            building_records[b_id]['town'] = val_t
        except:
            pass
        try:
            year = df.loc[df.iloc[:, 0].str.contains('construction year', case=False, na=False), 1].iloc[0]
            building_records[b_id]['construction_year'] = year
        except:
            pass
        try:
            floors = df[(df.iloc[:10, 2] > 0) & df.iloc[:, 1].str.contains('floor|ground', case=False, na=False)]
            # print(b_id, f'floors: ', floors)
            # print(b_id, f'length floors:', len(floors))
            if not floors.empty:
                building_records[b_id]['num_floors'] = str(len(floors))
                # print(b_id, str(len(floors)))
        except:
            pass
        try:
            total = df.loc[df.iloc[:, 1].str.contains('total', case=False, na=False), 2].iloc[0]
            building_records[b_id]['total_floor_area_m2'] = total
        except:
            pass
        try:
            total_o = df.loc[df.iloc[:, 1].str.contains('occupied', case=False, na=False), 2].iloc[0]
            building_records[b_id]['occupied_area_m2'] = total_o
        except:
            pass
        try:
            # check column 2 if it contains kwh/year then retrieve value on column where column 1 is total
            if parts[2] == 'table13':
                mask = df.loc[df.loc[:, 0].astype(str).str.contains('total', case=False, na=False), 1]
                if not mask.empty:
                    building_records[b_id]['energy use (kWh/yr)'] = mask.iloc[0]
        except:
            pass
        try:
            # check column 2 if it contains kg CO2/year then retrieve value on column where column 1 is total from file table  13
            if parts[2] == 'table13':
                mask = df.loc[df.loc[:, 0].astype(str).str.contains('total', case=False, na=False), 2]

                if not mask.empty:
                    building_records[b_id]['kg CO2/year'] = mask.iloc[0]
        except:
            pass
        try:
            total_air = df.loc[df.iloc[:, 1]=='Occupied with aircon', 2].iloc[0]
            building_records[b_id]['ac_area_m2'] = total_air
        except:
            pass
        try:
            total_ac = df.loc[df.iloc[:, 0]=='Air conditioning', 1].iloc[0]
            building_records[b_id]['has_ac'] = total_ac
        except:
            pass
        try:
            ac_area = df.loc[df.iloc[:, 0]=='Air conditioning', 2].iloc[0]
            building_records[b_id]['ac_coverage_ratio'] = ac_area
        except:
            pass

    except Exception as e:
        print(f'Error: {e}')
        continue


df = pd.DataFrame(building_records.values())
df['building_id'] = df['building_id'].astype(int)
print(len(df))

df.to_csv('./data/combined/clean_building_data.csv', index=False)

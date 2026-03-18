import pandas as pd


df = pd.read_csv('./data/combined/cleaned_geometry_building_data.csv')

# ensure numeric sorting
df['building_id'] = pd.to_numeric(df['building_id'], errors='coerce')

df = df.sort_values(by='building_id')

df['building_id'] = 'B' + df['building_id'].astype(int).astype(str).str.zfill(3)

df.to_csv('./data/combined/sorted_cleaned_geometry_building_data.csv', index=False)
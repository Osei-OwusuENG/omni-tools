import pandas as pd


df = pd.read_csv('./data/combined/clean_building_data.csv')

# ensure numeric sorting
df['building_id'] = pd.to_numeric(df['building_id'], errors='coerce')

df = df.sort_values(by='building_id')

df['building_id'] = 'B' + df['building_id'].astype(int).astype(str).str.zfill(3)

pd.set_option('display.max_rows', None)
print(df.drop('has_hot_water', axis=1))

df.to_csv('./data/combined/sorted_cleaned_building_data.csv', index=False)
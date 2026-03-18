import pandas as pd

df = pd.read_csv('./data/combined/sorted_cleaned_geometry_building_data.csv')

pd.set_option('display.max_rows', None)
print(df['building_id'])
print(len(df['building_id']))